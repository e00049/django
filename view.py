def fetch_values(request):

    all_objects      = YourTable.objects.all() 	    # Retrieve all objects from the table

    filtered_objects = YourTable.objects.filter(phone_number = 7358220899)     # Retrieve objects based on a condition

    single_object    = YourTable.objects.get(id=some_id)     # Retrieve a single object

    profile          = YourTable.object.create(user = user, phone_number = phone_number)  - Create an object

    delete_user      = YourTable.objects.get(id=1).delete()

    update           = YourTable.objects.filter(phone_number=phone_number).update(otp=str(random.randint(100000, 999999)))
    
    
