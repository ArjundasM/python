"""
| **@created on:** 28/3/2018,
| **@author:** Arjun das m,
| **@version:** v0.0.1
|
| **Description:**
| To create aws-image of running or stopped instances. Image having snapshots of all attached volumes.
|
"""

import boto3
import sys

print('Enter instance-id:')
instance_id = input()
print('Enter a name for image:')
image_name = input()
print('No reboot:[True| False] default:[True]')
reboot = input()
if reboot == 'True' or reboot == '':
    no_reboot = True
else:
    no_reboot = False
print('Do you want to dry-run:[True|False] default [False]')
dryrun = input()
if dryrun == 'True':
    do_dryrun = True
elif dryrun == '':
    do_dryrun = False
print('Enter a small description for the image:[Optional]')
description = input()


ec2 = boto3.resource('ec2')
id_list = [ids.id for ids in ec2.instances.all()]

def check_instance_id():
    if instance_id in id_list:
        return True

def create_image(ids, name='Example', description='Sample image', dryrun=False, reboot=True):
    instance = ec2.Instance(instance_id)
    image = instance.create_image(InstanceId= ids, Name= name, Description=description, DryRun=dryrun, NoReboot=reboot)
    print('Image created with id: ', image.id, 'with name: ', image_name)


if check_instance_id():
    print('Instance-Id is available in this region. Image creation going to start.')
    create_image(instance_id, image_name, description, do_dryrun, no_reboot)
else:
    print('Entered Instance-Id not avialable in this region.')
    print('The available Instance-Ids are: ',id_list)

#Valid arguments
# must be one of: BlockDeviceMappings, Description, DryRun, InstanceId, Name, NoReboot
