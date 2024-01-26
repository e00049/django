# Assign Cutom group for user while register. 

# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Add any additional fields you want to include in the registration

    groups = serializers.ListField(write_only=True)  # ListField to accept groups data

    class Meta:
        model = User
        fields = ['username', 'password', 'groups', ...]  # Add fields here

    def create(self, validated_data):
        # Extract the groups data from validated_data
        groups_data = validated_data.pop('groups', [])

        # Create the user object
        user = User.objects.create(**validated_data)

        # Assign groups to the user using set() method
        if groups_data:
            for group_name in groups_data:
                try:
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)
                except Group.DoesNotExist:
                    pass

        return user


# Types of Serializer Classes in Django REST Framework:

# 01. ModelSerializer
# 02. Serializer

# Types of Serializer Class Functions:

    # create (self, validated_data):
    # validate (self, attrs):
    # save(self, **kwargs):
    # get_tokens(self, obj):
    # update(self, instance, validated_data):
    # is_valid ()
    # save()

