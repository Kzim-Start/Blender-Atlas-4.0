# -*- coding: utf-8 -*-
"""Blender Atlas 4.0 — cenas editáveis e exemplos de modificadores.
No Blender: Workspace Scripting > Open > este arquivo > Run Script.
Altere CENA abaixo para: bau, espada, cerca, arvore, rocha, personagem, animacao.
Para gerar todas pelo terminal: blender -b --python gerar_cenas_atlas4.py -- --all
As cenas são didáticas, não são personagens finalizados prontos para um jogo.
"""
import bpy
import math
import sys
from pathlib import Path
from mathutils import Vector

CENA = 'bau'  # altere este valor para escolher a cena
PASTA = Path(bpy.path.abspath('//')).resolve() / 'CENAS_ATLAS4_GERADAS'
PASTA.mkdir(parents=True, exist_ok=True)


def material(nome, cor, metal=0.0, rugosidade=0.6):
    m=bpy.data.materials.new(nome)
    m.use_nodes=True
    bsdf=m.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value=(*cor,1)
    bsdf.inputs['Metallic'].default_value=metal
    bsdf.inputs['Roughness'].default_value=rugosidade
    return m


def cube(nome, xyz, escala, mat, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=xyz)
    o=bpy.context.object;o.name=nome
    o.dimensions=escala
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if mat:o.data.materials.append(mat)
    if bevel:
        mod=o.modifiers.new('Bordas suaves | Bevel','BEVEL')
        mod.width=bevel;mod.segments=3
        o.modifiers.new('Normais ponderadas','WEIGHTED_NORMAL')
    return o


def cylinder(nome,xyz,radius,depth,mat,verts=12):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=radius,depth=depth,location=xyz)
    o=bpy.context.object;o.name=nome
    if mat:o.data.materials.append(mat)
    return o


def create_room():
    floor=material('Chao neutro',(.095,.13,.16),0,.88)
    cube('Chao',(0,0,-.10),(16,16,.18),floor)
    bpy.ops.object.light_add(type='AREA',location=(0,-4,7))
    light=bpy.context.object;light.name='Luz principal';light.data.energy=1300;light.data.shape='DISK';light.data.size=7
    bpy.ops.object.camera_add(location=(6,-9,6))
    camera=bpy.context.object;camera.name='Camera de estudo'
    direction=Vector((0,0,1.2))-camera.location
    camera.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
    bpy.context.scene.camera=camera
    bpy.context.scene.render.engine='CYCLES'
    bpy.context.scene.cycles.samples=24
    bpy.context.scene.render.resolution_x=1000
    bpy.context.scene.render.resolution_y=740
    bpy.context.scene.render.resolution_percentage=100


def create_bau():
    wood=material('Madeira macica de estudo',(.34,.16,.075),0,.76)
    iron=material('Ferro forjado de estudo',(.095,.115,.13),1,.48)
    bronze=material('Fecho bronze',(.5,.29,.085),1,.32)
    cube('Corpo principal',(0,0,.77),(2.35,1.4,1.24),wood,.08)
    cube('Tampa',(0,0,1.49),(2.46,1.52,.28),wood,.07)
    for x in (-.86,.86):
        cube('Tira ferro frente', (x,-.715,.83),(.16,.055,1.3),iron,.024)
        cube('Tira ferro tampa',(x,-.74,1.50),(.17,.09,.30),iron,.017)
    for z in (.45,1.13):
        cube('Reforco frente',(0,-.735,z),(2.37,.06,.11),iron,.019)
    cube('Fechadura',(0,-.82,1.21),(.29,.11,.26),bronze,.02)
    # Demonstra Array nao destrutivo em uma fileira de rebites.
    rib=cylinder('Rebite + Array',(-.88,-.801,.47),.046,.04,bronze,16)
    rib.rotation_euler[0]=math.pi/2
    array=rib.modifiers.new('Repeticao precisa | Array','ARRAY')
    array.count=9;array.relative_offset_displace=(4.6,0,0)
    # Objetos informativos no Outliner


def create_espada():
    iron=material('Aco da lamina',(.52,.58,.64),1,.22)
    bronze=material('Guarda antiga',(.52,.32,.12),1,.4)
    leather=material('Couro do punho',(.13,.065,.035),0,.76)
    blade=cube('Lamina',(0,0,2.55),(.26,.10,3.4),iron,.018)
    blade.modifiers.new('Subsurf opcional (desativado)','SUBSURF').show_viewport=False
    cube('Guarda',(0,0,.85),(1.3,.24,.20),bronze,.06)
    cylinder('Punho',(0,0,.28),.12,.95,leather,12)
    cylinder('Pomo',(0,0,-.23),.18,.19,bronze,16)


def create_cerca():
    wood=material('Pinho bruto',(.38,.23,.11),0,.86)
    iron=material('Parafusos',(.12,.12,.12),1,.66)
    stick=cube('Uma estaca + Array',(-2.2,0,1.1),(.35,.36,2.2),wood,.028)
    arr=stick.modifiers.new('Array de 12 estacas','ARRAY')
    arr.count=12
    arr.use_relative_offset=False
    arr.use_constant_offset=True
    arr.constant_offset_displace=(.48,0,0)
    for z in (.63,1.68):cube('Travessa',(.40,-.24,z),(6,.16,.22),wood,.024)


def create_arvore():
    bark=material('Casca cinza',(.23,.18,.13),0,.93)
    leaf=material('Folhas verdes',(.09,.29,.11),0,.80)
    trunk=cylinder('Tronco principal',(0,0,1.55),.4,3.1,bark,10)
    sub=trunk.modifiers.new('Subdivisao leve','SUBSURF');sub.levels=1
    for x,y,z,s in [(0,0,3.25,1.32),(-1.05,0,2.72,.85),(1.10,.2,2.87,.97),(.23,.85,3.45,.78)]:
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2,radius=s,location=(x,y,z))
        o=bpy.context.object;o.name='Copa verde | bloco low-poly';o.data.materials.append(leaf)


def create_rocha():
    stone=material('Pedra cinza',(.26,.29,.31),0,.9)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2,radius=1.25,location=(0,0,1.18))
    o=bpy.context.object;o.name='Pedra base';o.scale=(1.25,.75,1.15)
    o.data.materials.append(stone)
    tex=bpy.data.textures.new('Noise para Displace',type='CLOUDS');tex.noise_scale=.5
    sub=o.modifiers.new('Mais geometria','SUBSURF');sub.levels=2
    disp=o.modifiers.new('Variacao superficial','DISPLACE');disp.texture=tex;disp.strength=.13


def create_personagem():
    cloth=material('Robe azul',(.06,.24,.43),0,.71)
    skin=material('Pele stylized',(.61,.37,.22),0,.71)
    hat=material('Chapeu azul escuro',(.035,.12,.25),0,.71)
    cube('Tronco | placeholder',(0,0,1.25),(.87,.54,1.25),cloth,.13)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,radius=.38,location=(0,0,2.25))
    bpy.context.object.name='Cabeca';bpy.context.object.data.materials.append(skin)
    for x in (-.63,.63):
        cube('Braco',(x,0,1.39),(.29,.34,1.0),cloth,.08)
    for x in (-.25,.25):cube('Perna',(x,0,.38),(.32,.38,.79),hat,.055)
    bpy.ops.mesh.primitive_cone_add(vertices=16,radius1=.58,radius2=.03,depth=.75,location=(0,0,2.82))
    bpy.context.object.name='Chapeu';bpy.context.object.data.materials.append(hat)
    # Armature didatica, sem deformacao automatica para nao criar promessa enganosa
    bpy.ops.object.armature_add(enter_editmode=False,location=(0,0,0))
    arm=bpy.context.object;arm.name='Armature exemplo | vincule manualmente'
    arm.show_in_front=True


def create_animacao():
    red=material('Esfera laranja',(.94,.27,.05),0,.34)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=16,radius=.7,location=(-3,0,1))
    o=bpy.context.object;o.name='Bola animada'
    o.data.materials.append(red)
    for frame,x,z in ((1,-3,1),(13,0,3),(25,3,1)):
        o.location=(x,0,z);o.keyframe_insert(data_path='location',frame=frame)
    bpy.context.scene.frame_start=1;bpy.context.scene.frame_end=25
    bpy.context.scene.frame_set(1)

builders={'bau':create_bau,'espada':create_espada,'cerca':create_cerca,'arvore':create_arvore,'rocha':create_rocha,'personagem':create_personagem,'animacao':create_animacao}

def build(name):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    create_room()
    builders[name]()
    bpy.ops.wm.save_as_mainfile(filepath=str(PASTA/(name+'_atlas4.blend')))
    print('Cena salva:',PASTA/(name+'_atlas4.blend'))

names=list(builders) if '--all' in sys.argv else [CENA]
for item in names:
    if item not in builders: raise ValueError('Cena invalida. Use: '+', '.join(builders))
    build(item)
