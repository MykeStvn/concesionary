from django.db import models

# MODELS
#City
class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    name_city = models.CharField(max_length=255)
    #ocupo este Meta porque en la base de datos al crear un nuevo 
    #me da un error de nombrado de tabla
    class Meta:
        db_table = 'city' 
    def save(self, *args, **kwargs):
        # Convertimos el nombre de la ciudad a mayúsculas antes de guardar
        self.name_city = self.name_city.upper()
        # Llamamos al método save() del modelo para guardar la ciudad
        super(City, self).save(*args, **kwargs)
    def __str__(self):
        return self.name_city

#Model
class Model (models.Model):
    id_model = models.AutoField(primary_key=True)
    name_model = models.CharField(max_length=255)
    #renombro a la tabla porque se guardaba como Company_model
    class Meta:
        db_table = 'model' 
    def save (self, *args, **kwargs):
        #Convertir el nombre de modelo en MAYUSCULA
        self.name_model = self.name_model.upper()
        # llamo al metodo SAVE() para guardar
        super(Model, self).save(*args, **kwargs)
    def __str__(self):
        return self.name_model
    
#Propierty
class Propierty (models.Model):
    id_prop = models.AutoField(primary_key=True)
    name_prop = models.CharField(max_length=255)    
    last_name_prop = models.CharField(max_length=255)    
    email_prop = models.CharField(max_length=255)    
    phone_prop = models.CharField(max_length=255)    
    #Relationship of foreign key whit table City
    fk_id_city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True, blank=True,db_column='fk_id_city')
    class Meta:
        db_table = 'propierty'

    def __str__(self):
        return f"{self.name_prop} {self.last_name_prop}"

    def save(self, *args, **kwargs):
        # Convertir todos los campos de texto a mayúsculas antes de guardar
        self.name_prop = self.name_prop.upper()
        self.last_name_prop = self.last_name_prop.upper()
        self.email_prop = self.email_prop.upper()
        self.phone_prop = self.phone_prop.upper()
        
        # Llamar al método save() de la clase base para guardar el objeto
        super(Propierty, self).save(*args, **kwargs)


#Vehicle
class Vehicle(models.Model):
    id_veh = models.AutoField(primary_key=True)
    year_fabrication_veh = models.IntegerField
    price_veh = models.DecimalField(max_digits=10, decimal_places=2)
    color_veh = models.CharField(255)
    plate_veh = models.CharField(255)
    #Relationship of foreign key with table Property
    #DJANGO POR CONVENSIÓN PONE OTRO NOMBRE POR LO CUAL
    #SE COLOCA EN LOS PARAMETROS UN db_column
    #CON LO CUAL ASIGNO A MI COLUMNA EL NOMBRE QUE DESEO
    fk_id_prop = models.ForeignKey(Propierty, on_delete=models.SET_NULL,null=True, blank=True,db_column='fk_id_prop') 
    #Relationship of foreign key with table Model
    fk_id_model = models.ForeignKey(Model, on_delete=models.SET_NULL,null=True, blank=True,db_column='fk_id_model')
    class Meta:
        db_table = 'vehicle' 
    def __str__(self):
        return f"{self.id_veh} {self.last_name_prop}"