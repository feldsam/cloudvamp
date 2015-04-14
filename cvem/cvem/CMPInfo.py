# -------------------------------------------------------------------------- #
# Copyright 2015, Universitat Politecnica de Valencia                        #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
#--------------------------------------------------------------------------- #

from config import Config

class CMPInfo:
	"""
	Base class to the CMP information classes
	"""

	@staticmethod
	def get_vm_list():
		"""
		Get the list of VMs of the CMP
		
		Return: list of VirtualMachineInfo
		"""
		raise Exception("Not implemented")
	
	@staticmethod
	def get_host_info(host_id):
		"""
		Get the information about the host "host_id"
		
		Args:

		- host_id: Host id.

		Return: HostInfo object
		"""
		raise Exception("Not implemented")
	
	@staticmethod
	def get_host_list():
		"""
		Get the information about the host "host_id"

		Return: list of HostInfo
		"""
		raise Exception("Not implemented")
	
	@staticmethod
	def migrate(vm_id, host_id):
		"""
		Migrate the VM "vm_id" to the Host "host_id" 
		
		Args:
		- vm_id: VM id.
		- host_id: Host id.

		Return: True if the migration was performed successfully or False otherwise 
		"""
		raise Exception("Not implemented")

class VirtualMachineInfo:
	""" Class to store the VM information """
	def __init__(self, id = None, host = None, allocated_memory = None, raw = None):
		self.id =  id
		self.host =  host
		self.user_id = None
		""" User ID owner of the VM """
		self.real_memory =  None
		""" Real memory assigned to the VM """
		self.total_memory =  None
		""" Total memory reported by the S.O. (less than real_memory) """
		self.free_memory =  None
		""" Free memory of the VM """
		self.allocated_memory = None
		""" Amount of memory originally allocated by the CMP """
		self.raw = raw
		""" Data of the VM in the original format of the CMP """
	
	def set_memory_values(self, real_memory, total_memory, free_memory):
		"""
		Set the memory monitored values of the VM.
		For the free_memory it is corrected using the configuration value: SYS_MEM_OFFSET 
		
		Args:
		- real_memory(int): Real memory assigned to the VM. 
		- total_memory(int): Total memory reported by the S.O.
		- free_memory(int): Free memory of the VM.
		"""
		self.real_memory =  real_memory
		self.total_memory =  total_memory
		self.free_memory =  free_memory - Config.SYS_MEM_OFFSET
		
class HostInfo:
	""" Class to store the Host information """
	def __init__(self, id = None, name = None, raw = None):
		self.id =  id
		self.name =  name
		self.raw = raw
		""" Data of the host in the original format of the CMP """