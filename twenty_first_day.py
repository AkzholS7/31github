#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

from pyVim import connect
from pyVmomi import vim
import datetime

def connect_vcenter():
    # Connect to vCenter Server
    try:
        service_instance = connect.SmartConnectNoSSL(
            host='vcenter_hostname_or_IP',
            user='username',
            pwd='password'
        )
        return service_instance.RetrieveContent()
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def get_all_vms(content):
    # Get all VMs
    container = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.VirtualMachine], True
    )
    return container.view

def power_off_vms(vms):
    # Power off all VMs
    for vm in vms:
        try:
            print(f"Powering off VM: {vm.name}")
            vm.PowerOff()
        except Exception as e:
            print(f"Failed to power off {vm.name}: {e}")

def main():
    # Connect to vCenter Server
    content = connect_vcenter()
    if not content:
        return

    # Get current day of the week (0=Monday, 6=Sunday)
    current_day = datetime.datetime.now().weekday()

    # If it's Saturday (5) or Sunday (6), shut down all VMs
    if current_day == 5 or current_day == 6:
        all_vms = get_all_vms(content)
        power_off_vms(all_vms)

    # Disconnect from vCenter Server
    connect.Disconnect(content)

if __name__ == "__main__":
    main()
