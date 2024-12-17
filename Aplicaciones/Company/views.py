from django.contrib import messages  # Asegúrate de importar el módulo de mensajes de Django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#esta va a cargar mis modelos city,model,propierty,vehicle
from Aplicaciones.Company.models import City, Model, Propierty, Vehicle

def inicio(request):
    return render(request,"inicio.html")
#INICIO CIUDADES
#Renderización del template listadoCiudades
def listadoCiudades(request):
    cityBdd = City.objects.all()
    return render(request,"listadoCiudades.html",{'city':cityBdd})
#Insercción de ciudad
def agregar_ciudad(request):
    if request.method == 'POST':
        city_name = request.POST.get('name_city')

        # Verificar si ya existe una ciudad con el mismo nombre
        if City.objects.filter(name_city__iexact=city_name).exists():  # `iexact` para evitar diferencia entre mayúsculas y minúsculas
            # Si ya existe, mostrar un mensaje de error
            messages.error(request, "¡La ciudad ya existe! Ingrese un nombre único.")
            return redirect('listadoCiudades')  # Redirige de vuelta al listado de ciudades con el mensaje de error
        else:
            # Si no existe, crear la nueva ciudad
            new_city = City(name_city=city_name)
            new_city.save()
            return redirect('listadoCiudades')  # Redirige a la lista de ciudades después de agregarla

    return render(request, 'listadoCiudades.html')  # Si no es POST, simplemente renderiza el formulario
#Actualización de ciudad
#dame los datos de ciudad
def get_city_data(request):
    # Obtener el parámetro 'id' de la solicitud
    city_id = request.GET.get('id')
    
    # Validar si se proporcionó un id
    if not city_id:
        return JsonResponse({'error': 'No se proporcionó identificación de ciudad'}, status=400)

    try:
        # Buscar la ciudad en la base de datos usando 'id_city'
        city = City.objects.get(id_city=city_id)  # Usamos 'id_city' en lugar de 'id'
        
        # Devolver los datos de la ciudad en formato JSON
        return JsonResponse({
            'id_city': city.id_city,
            'name_city': city.name_city
        })
    except City.DoesNotExist:
        return JsonResponse({'error': 'Ciudad no encontrada'}, status=404)
    except Exception as e:
        # Capturar cualquier otra excepción inesperada y devolver un error genérico
        return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)

#actualizame los datos
@csrf_exempt
def update_city(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        city_id = request.POST.get('id_city')
        name_city = request.POST.get('name_city')
        
        # Validamos si los datos necesarios están presentes
        if not city_id or not name_city:
            return JsonResponse({'error': 'Falta el ID o el nombre de la ciudad'}, status=400)

        try:
            # Buscamos la ciudad usando 'id_city' en lugar de 'id'
            city = City.objects.get(id_city=city_id)
            
            # Actualizamos el nombre de la ciudad
            city.name_city = name_city
            city.save()
            
            # Si todo sale bien, devolvemos una respuesta exitosa
            return JsonResponse({'status': 'success'})
        
        except City.DoesNotExist:
            return JsonResponse({'error': 'Ciudad no encontrada'}, status=404)
        except Exception as e:
            # Si ocurre algún error inesperado, lo capturamos y lo mostramos
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)

#Eliminar una ciudad
@csrf_exempt
def delete_city(request):
    if request.method == 'POST':
        # Obtenemos el id de la ciudad desde la solicitud
        city_id = request.POST.get('id_city')

        if not city_id:
            return JsonResponse({'error': 'Se requiere identificación de la ciudad'}, status=400)

        try:
            # Buscamos y eliminamos la ciudad
            city = City.objects.get(id_city=city_id)
            city.delete()  # Eliminamos la ciudad
            
            return JsonResponse({'status': 'success'})
        
        except City.DoesNotExist:
            return JsonResponse({'error': 'CIudad no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)
#FIN CIUDADES

#INICIO MODELOS
#Listado de los datos bdd
def listadoModelos(request):
    modelBdd = Model.objects.all()
    return render(request,"listadoModelos.html",{'model':modelBdd})
#Insercción en modelo
def agregar_modelo(request):
    if request.method == 'POST':
        model_name = request.POST.get('name_model')
        #verfico si ya existe un modelo con el mismo nombre
        if Model.objects.filter(name_model__iexact=model_name).exists():
            messages.error(request, "¡EL modelo ya existe! INgrese un nombre único.")
            return redirect('listadoModelos')#Redirige de vuelta al listado de modelos con el mensaje de error
        else:
            #Si no existe, crear un nuevo modelo
            new_model = Model(name_model=model_name)
            new_model.save()
            return redirect('listadoModelos')#Redirige a la lista de modelos después de agregar el nuevo modelo
    return redirect(request, 'listadoModelos.html') #SI no es POST, simplemente renderiza el formulario
#Actualización de modelo
#dame los datos de modelo
def get_model_data(request):
    #Obtener el parámetro 'id' de la solicitud
    model_id = request.GET.get('id')
    #Validar si se proporcionó un id
    if not model_id:
        return JsonResponse({'error':'No se proporcionó identificación de modelo'}, status=400)
    try:
        #Buscar el modelo en la bdd 'id_model'
        model = Model.objects.get(id_model=model_id)#va el id_city
        #devuelvo los datos del modelo en JSON
        return JsonResponse({
            'id_model': model.id_model,
            'name_model': model.name_model
        })
    except Model.DoesNotExist:
        return JsonResponse({'error':'Modelo no encontrado'},status=400)
    except Exception as e:
        #Capturo cualquier otra excepción inesperada y devuelvo
        return JsonResponse({'error':f'Error al procesar la solicitud: {str(e)}'},status=500)
#Actualizando los datos
@csrf_exempt #token
def update_model(request):
    if request.method == 'POST':
        #Obtenemos los datos del formulario
        model_id = request.POST.get('id_model')
        name_model = request.POST.get('name_model')
        #validamos si los datos necesarios están presentes
        if not model_id or not name_model:
            return JsonResponse({'error':'Falta el ID o el nombre del modelo'})
        try: 
            #Buscamos el modelo usando 'id_model' en lugar de 'id'
            model = Model.objects.get(id_model=model_id)
            #Actualizamos el nombre del modelo
            model.name_model = name_model
            model.save()
            #SI todo sale correcto, devolvemos un mensaje de respuesta exitoso
            return JsonResponse({'status':'success'})
        except Model.DoesNotExist:
            return JsonResponse({'error':'Modelo no encontrado'}, status=400)
        except Exception as e:
            #Si ocurre algun error insesperado, lo capturamos
            return JsonResponse({'error':f'Erro al procesar la solicitud: {str(e)}'},status=500)
#ELiminar modelo
@csrf_exempt
def delete_model(request):
    if request.method == 'POST':
        #Obtenemos el ID del modelo desde la solicitud
        model_id = request.POST.get('id_model')

        if not model_id:
            return JsonResponse({'error':'Se requiere identificación del modelo'}, status=400)
        try:
            #Buscamos y eliminamos el modelo
            model = Model.objects.get(id_model=model_id)
            model.delete() #ELiminamos el modelo
            
            return JsonResponse({'status': 'success'})
        
        except Model.DoesNotExist:
            return JsonResponse({'error':'Modelo no encontrado'}, status=404)
        #Por si existe algun error inesperado
        except Exception as e:
            return JsonResponse({'error':f'Error al procesar la solicitud: {str(e)}'},status=500)
#FIN MODELOS

#INICIO PROPIERTY
#Renderización del template listadoPropietarios
def listadoPropietarios(request):
    propertyBdd = Propierty.objects.all()
    cityBdd = City.objects.all()
    return render(request, "listadoPropietarios.html", {'property': propertyBdd, 'city': cityBdd})

# Vista para agregar una propiedad
def add_propierty(request):
    if request.method == 'POST':
        name = request.POST.get('name_prop')
        last_name = request.POST.get('last_name_prop')
        email = request.POST.get('email_prop')
        phone = request.POST.get('phone_prop')
        fk_id_city = request.POST.get('fk_id_city')

        # Verificar que fk_id_city no esté vacío y que sea un valor válido
        if fk_id_city:
            try:
                # Buscar el objeto City correspondiente al ID recibido
                city = City.objects.get(id_city=fk_id_city)
            except City.DoesNotExist:
                # Si no existe la ciudad, devolver un error
                return JsonResponse({'status': 'error', 'message': 'City not found'})
        else:
            # Si fk_id_city no es proporcionado o está vacío, devolver un error
            return JsonResponse({'status': 'error', 'message': 'Please select a valid city'})

        # Crear un nuevo objeto Propierty con el objeto city
        Propierty.objects.create(
            name_prop=name,
            last_name_prop=last_name,
            email_prop=email,
            phone_prop=phone,
            fk_id_city=city  # Asignar el objeto City, no solo el ID
        )

        # Después de crear la propiedad, redirigir al listado de propietarios
        return redirect('listadoPropietarios')

    # Si no es una solicitud POST, redirigir normalmente
    return redirect('listadoPropietarios')

# Vista para obtener los datos de una propiedad para editar
def get_propierty_data(request):
    prop_id = request.GET.get('id')
    prop = get_object_or_404(Propierty, id_prop=prop_id)
    return JsonResponse({
        'id_prop': prop.id_prop,
        'name_prop': prop.name_prop,
        'last_name_prop': prop.last_name_prop,
        'email_prop': prop.email_prop,
        'phone_prop': prop.phone_prop,
        'fk_id_city': prop.fk_id_city.id_city,  # Ciudad seleccionada
    })

# Vista para actualizar los datos de una propiedad
def update_propierty(request):
    if request.method == 'POST':
        prop_id = request.POST.get('id_prop')
        prop = get_object_or_404(Propierty, id_prop=prop_id)

        # Actualizar los datos de la propiedad
        prop.name_prop = request.POST.get('name_prop')
        prop.last_name_prop = request.POST.get('last_name_prop')
        prop.email_prop = request.POST.get('email_prop')
        prop.phone_prop = request.POST.get('phone_prop')
        prop.fk_id_city_id = request.POST.get('fk_id_city')

        # Guardar la propiedad
        prop.save()

        # Devolver los nuevos datos actualizados para actualizar la tabla en el frontend
        return JsonResponse({
            'status': 'success',
            'id_prop': prop.id_prop,
            'name_prop': prop.name_prop,
            'last_name_prop': prop.last_name_prop,
            'email_prop': prop.email_prop,
            'phone_prop': prop.phone_prop,
            'city': prop.fk_id_city.name_city  # Asumiendo que la propiedad 'fk_id_city' es un objeto relacionado con la ciudad
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# Vista para eliminar una propiedad
def delete_propierty(request):
    if request.method == 'POST':
        prop_id = request.POST.get('id_prop')
        prop = get_object_or_404(Propierty, id_prop=prop_id)
        prop.delete()
        return JsonResponse({'status': 'success'})
#FIN PROPIERTY

#INICIO VECHILE
#Renderización del template listadoVehiculos
def listadoVehiculos(request):
    vehicleBdd = Vehicle.objects.all()
    propertyBdd = Propierty.objects.all()
    modelBdd = Model.objects.all()
    return render(request,"listadoVehiculos.html",{'vehicle':vehicleBdd,'property':propertyBdd,'model':modelBdd})
        
#AÑADIR UN NUEVO VEHICULO
def add_vehicle(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        year_fabrication_veh = request.POST.get('year_fabrication_veh')
        price_veh_str = request.POST.get('price_veh', '').strip()
        color_veh = request.POST.get('color_veh')
        plate_veh = request.POST.get('plate_veh')
        fk_id_prop = request.POST.get('fk_id_prop')
        fk_id_model = request.POST.get('fk_id_model')

        # Validar que el precio no esté vacío y que sea un valor válido
        if not price_veh_str:
            return JsonResponse({'status': 'error', 'message': 'Price is required'})

        try:
            price_veh = Decimal(price_veh_str)
        except InvalidOperation:
            return JsonResponse({'status': 'error', 'message': 'Invalid price format'})

        # Validar que el año de fabricación no esté vacío y sea un número entero
        if not year_fabrication_veh:
            return JsonResponse({'status': 'error', 'message': 'Year of fabrication is required'})

        try:
            year_fabrication_veh = int(year_fabrication_veh)
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid year format'})

        # Verificar que fk_id_prop no esté vacío y sea un valor válido
        if fk_id_prop:
            try:
                prop = Propierty.objects.get(id_prop=fk_id_prop)
            except Propierty.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Property not found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Property is required'})

        # Verificar que fk_id_model no esté vacío y sea un valor válido
        if fk_id_model:
            try:
                model = Model.objects.get(id_model=fk_id_model)
            except Model.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Model not found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Model is required'})

        # Crear un nuevo vehículo
        Vehicle.objects.create(
            year_fabrication_veh=year_fabrication_veh,
            price_veh=price_veh,
            color_veh=color_veh,
            plate_veh=plate_veh,
            fk_id_prop=prop,  # Asignar el objeto Propierty, no solo el ID
            fk_id_model=model,  # Asignar el objeto Model, no solo el ID
        )

        # Redirigir a la lista de vehículos
        return redirect('listadoVehiculos')

    # Si no es una solicitud POST, redirigir normalmente
    return redirect('listadoVehiculos')

# Vista para obtener los datos de una propiedad para editar
def get_vehicle_data(request):
    veh_id = request.GET.get('id_veh')
    veh = get_object_or_404(Vehicle, id_veh=veh_id)
    return JsonResponse({
        'id_veh': veh.id_veh,
        'year_fabrication_veh': veh.year_fabrication_veh,
        'price_veh': veh.price_veh,
        'color_veh': veh.color_veh,
        'plate_veh': veh.plate_veh,
        'fk_id_model': veh.fk_id_model.id_model,  # Modelo seleccionada
        'fk_id_prop': veh.fk_id_prop.id_prop  # Modelo seleccionada
    })


# Vista para actualizar los datos de una propiedad
def update_vehicle(request):
    if request.method == 'POST':
        # Obtener el ID del vehículo
        vehicle_id = request.POST.get('id_veh')
        vehicle = get_object_or_404(Vehicle, id_veh=vehicle_id)

        # Actualizar los datos del vehículo
        vehicle.year_fabrication_veh = request.POST.get('year_fabrication_veh')
        vehicle.price_veh = request.POST.get('price_veh')
        vehicle.color_veh = request.POST.get('color_veh')
        vehicle.plate_veh = request.POST.get('plate_veh')

        # Obtener las claves foráneas relacionadas
        fk_id_prop = request.POST.get('fk_id_prop')
        fk_id_model = request.POST.get('fk_id_model')

        # Validar y asignar propiedad relacionada
        if fk_id_prop:
            vehicle.fk_id_prop_id = fk_id_prop  # Usamos `_id` para asignar directamente la clave foránea
        
        # Validar y asignar modelo relacionado
        if fk_id_model:
            vehicle.fk_id_model_id = fk_id_model  # Usamos `_id` para asignar directamente la clave foránea

        # Guardar el vehículo actualizado
        vehicle.save()

        # Devolver los datos actualizados para el frontend
        return JsonResponse({
            'status': 'success',
            'id_veh': vehicle.id_veh,
            'year_fabrication_veh': vehicle.year_fabrication_veh,
            'price_veh': vehicle.price_veh,
            'color_veh': vehicle.color_veh,
            'plate_veh': vehicle.plate_veh,
            'prop_name': vehicle.fk_id_prop.name_prop if vehicle.fk_id_prop else None,
            'model_name': vehicle.fk_id_model.name_model if vehicle.fk_id_model else None
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# Vista para eliminar una propiedad
def delete_vehicle(request):
    if request.method == 'POST':
        veh_id = request.POST.get('id_veh')
        veh = get_object_or_404(Vehicle, id_veh=veh_id)
        veh.delete()
        return JsonResponse({'status': 'success'})

#FIN VEHICLE