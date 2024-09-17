

class HandleErrorsService:
  error = None
  statusCode = None
  def __init__(self, error=None, statusCode=None):
    self.set_error(error, statusCode)

  def set_error(self, error, statusCode):
    self.error = error
    self.statusCode = statusCode
    
  def get_error(self):
    if self.statusCode is None and self.error is not None:
      return {"message": self.error}
    
    if self.error is None:
      return {"message": "Internal server error"}
    
    return {"message": self.error}, self.statusCode
    