##coding=utf8
#from Mech_setting import *
#import json

## 武器信息读取
#weapon_information = {}
#weapon_information['cd_speed'] = 1
#weapons = []
#for i in xrange(1,13):
#    weapon = {}
#    weapon['weapon_name'] = name_Weapon[i]
#    weapon['bullet_name'] = name_Bullet[i]
#    weapon['bullet_capacity'] = Ammo_Weapon[i]
#    weapon['cd'] = coolingTime_Weapon[i]
#    weapon['inaccuracy'] = inaccuracy_Weapon[i]
#    weapon['rotation_speed'] = rotationSpeed_Weapon[i]
#    weapon['speed'] = speed_Bullet[i]
#    weapon['damage'] = damage_Bullet[i]
#    weapon['fly_time'] = flyTime_Bullet[i]
#    weapon['radius'] = radium_Weapon[i]


#    if name_Weapon[i] == 'Shotgun':
#        weapon['burst'] = 5
#        weapon['gapRotation'] = 3

#    if name_Weapon[i] == 'Mine Layer':
#        weapon['explode_range'] = explodeR_Mine
#        weapon['mine_cd'] = 20
#        weapon['mine_capacity'] = 5

#    if name_Weapon[i] == 'R.P.G.':
#        weapon['explode_range'] = explodeR_RPGBall
#        weapon['bullet_acceleration'] = acceleration_RPGBall

#    if name_Weapon[i] == 'Grenade Thrower':
#        weapon['explode_range'] = explodeR_Grenade

#    if name_Weapon[i] == 'Plasma torch':
#        weapon['bounce_count'] = bounce_time

#    if name_Weapon[i] == 'Missile launcher':
#        weapon['bullet_rotation_speed'] = spinSpeed_TrackingMissile
#    weapons.append(weapon)

#weapon_information['weapons'] = weapons

## 机甲信息读取
#engine_information = {}
#engines = []
#for i in xrange(1,9):
#    engine = {}
#    engine['name'] = name_Engine[i]
#    engine['max_speed'] = maxSpeed_Engine[i]
#    engine['max_hp'] = maxHp_Engine[i]
#    engine['rotation_speed'] = rotationSpeed_Engine[i]
#    engine['acceleration'] = acceleration_Engine[i]
#    engine['radius'] = radium_Engine[i]
#    engines.append(engine)

#engine_information['engines'] = engines

## 建筑信息读取
#build_information = {}
#builds = []
#builds.append({
#    'radius':radium_Arsenal, 
#    'respawn_time':respawningTime_Arsenal, 
#    'build_name':u'圆形障碍物'
#    })
#build_information['builds'] = builds

## 汇总
#information = {
#    'weapon':weapon_information,
#    'engine':engine_information,
#    'build':build_information
#    }

#open('data.json','w').write(json.dumps(information,ensure_ascii=False))