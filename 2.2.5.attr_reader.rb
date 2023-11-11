class Person
  def initialize(name, job)
    attr_reader :name
    attr_writer :job
  end
  
  def name
    @name
  end
  
  def job=(new_job)
    @job = new_job
  end
end