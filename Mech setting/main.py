#coding=utf8
from Mech_setting import *

information = {}
weapon_information['cd_speed'] = 1

weapons = []
for i in xrange(1,13):
    weapon = {}
    weapon['weapon_name'] = name_Weapon[i]
    weapon['bullet_name'] = name_Bullet[i]
    weapon['bullet_capacity'] = Ammo_Weapon[i]
    weapon['cd'] = coolingTime_Weapon[i]
    weapon['inaccuracy'] = inaccuracy_Weapon[i]
    weapon['rotation_speed'] = rotationSpeed_Weapon[i]
    weapon['speed'] = speed_Bullet[i]
    weapon['damage'] = damage_Bullet[i]
    weapon['fly_time'] = flyTime_Bullet[i]



    if name_Weapon == 'Shotgun':
        weapon['burst'] = 5
        weapon['gapRotation'] = 3

    if name_Weapon == 'Mine Layer':
        weapon['mine_cd'] = 20
        weapon['mine_capacity'] = 5

engine_information = {}

engines = []
for i in xrange(1,9):
    engine = {}
    engine['name'] = name_Engine[i]
    engine['max_speed'] = maxSpeed_Engine[i]
    engine['max_hp'] = maxHp_Engine[i]
    engine['rotation_speed'] = rotationSpeed_Engine[i]
    engine['acceleration'] = acceleration_Engine[i]
    engine['range'] = radium_Engine[i]


