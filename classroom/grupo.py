from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo prederterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    def __str__(self):
      cadena= "Grupo de estudiantes: " + self._grupo
      return cadena

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
          
          self._asignaturas.append(Asignatura(x))
    
    def agregarAlumno(self, alumno, lista=None):
      if(lista is None):
        lista=[]
      lista.append(alumno)
      self.listadoAlumnos = self.listadoAlumnos + lista
      
      
        
       
     

    @classmethod
    def asignarNombre(*args):
      for arg in args:
        if arg == "Grado 1":
          Grupo.grado="Grado 1"
        else:
          Grupo.grado="Grado 6"

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 6"):
     #   cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 4"):
     #   cls.grado = nombre