from abc import ABC, abstractmethod

class AuditTrail:
    def record(self):
        print("Audit Trail")
        
#********************************************************************       
class Task(ABC):
    def __init__(self,auditTrail : AuditTrail):
        self.__auditTrail = auditTrail
        
    def execute(self):
        self.__auditTrail.record(self)
        self._doExecute()
        
    @abstractmethod    
    def _doExecute(self):
        pass

class TransferMonyTask(Task):
    def _doExecute(self):
        print("Transfer Mony")
        
#********************************************************************        
task = TransferMonyTask(AuditTrail)
task.execute()