from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from . import functions 
from .models import Project, Recipe, Material, Inventory, Step
import json
from django.views.decorators.csrf import csrf_protect

# Create your views here.


@login_required
@csrf_protect
def getUserInfo(request):
    tempuser = {
       'username': request.user.username, 
    }
    user = json.dumps(tempuser)
    return HttpResponse(user, content_type = 'application/json')

@login_required
@csrf_protect
def allProjects(request):
    userid = request.user.id
    if (request.method == 'GET'):
        projects = functions.getAllProjects(userid)
        return HttpResponse(projects, content_type = 'application/json')

    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        project = Project(
                name = body['name'], 
                description = body['description'], 
                notes = body['notes'],
                status = body['status'],
                image = body['image'],
                user_id = userid,
            )

        project.save()

        recipeArray = body['recipes']
        for recipe in recipeArray:
            recipeObject = Recipe.objects.get(pk = recipe['value'])
            recipeObject.projects.add(project)
        
        return HttpResponse("POST request successful")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def projectById(request, id):
    userid = request.user.id
    if (request.method == 'GET'):
        project = Project.objects.get(pk = id)
        projectData = functions.getProjectById(id)
        valueid = project.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            return HttpResponse(projectData, content_type = 'application/json')

    elif (request.method == 'PUT'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        project =  Project.objects.get(pk = id)
        valueid = project.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            project.name = body['name']
            project.description = body['description']
            project.notes = body['notes']
            project.image = body['image']
            project.recipe_set.clear()

            recipeArray = body['recipes']
            for recipe in recipeArray:
                recipeObject = Recipe.objects.get(pk = recipe['value'])
                recipeObject.projects.add(project)
            
            project.save()

            return HttpResponse("PUT Request to Project by ID")

    elif (request.method == 'DELETE'):
        project = Project.objects.get(pk = id)
        valueid = project.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            project.delete()
            return HttpResponse("DELETE Request to Project by ID")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def allRecipes(request):
    userid = request.user.id
    if (request.method == 'GET'):
        recipes = functions.getAllRecipes(userid)
        return HttpResponse(recipes, content_type = 'application/json')

    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        recipe = Recipe(
                name = body['name'], 
                description = body['description'],
                user_id = userid,
            )
        
        recipe.save()

        projectArray = body['projects']
        for project in projectArray:
            projectObject = Project.objects.get(pk = project['value'])
            projectObject.recipe_set.add(recipe)

        return HttpResponse("POST request successful")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def recipeById(request, id):
    userid = request.user.id
    if (request.method == 'GET'):
        return HttpResponse("GET Request to Recipe by ID")

    elif (request.method == 'PUT'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        recipe =  Recipe.objects.get(pk = id)
        valueid = recipe.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            recipe.name = body['name']
            recipe.description = body['description']
            recipe.projects.clear()

            projectArray = body['projects']
            for project in projectArray:
                projectObject = Project.objects.get(pk = project['value'])
                projectObject.recipe_set.add(recipe)
            
            recipe.save()

            return HttpResponse("PUT Request to Recipe by ID")

    elif (request.method == 'DELETE'):
        recipe = Recipe.objects.get(pk = id)
        valueid = recipe.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            recipe.delete()
            return HttpResponse("DELETE Request to Recipe by ID")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def allMaterials(request):
    userid = request.user.id
    if (request.method == 'GET'):
        materials = functions.getAllMaterials(userid)
        return HttpResponse(materials, content_type = 'application/json')

    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        material = Material(
                name = body['name'], 
                partNumber = body['partNumber'], 
                company = body['company'], 
                link = body['link'], 
                category = body['category'],
                user_id = userid,
            )
 
        material.save()

        return HttpResponse("POST request successful")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def materialById(request, id):
    userid = request.user.id
    if (request.method == 'GET'):
        return HttpResponse("GET Request to Material by ID")

    elif (request.method == 'PUT'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        material =  Material.objects.get(pk = id)
        valueid = material.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            material.name = body['name']
            material.partNumber = body['partNumber']
            material.company = body['company']
            material.link = body['link']
            
            material.save()
            return HttpResponse("PUT Request to Material by ID")

    elif (request.method == 'DELETE'):
        material = Material.objects.get(pk = id)
        valueid = material.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            material.delete()
            return HttpResponse("DELETE Request to Material by ID")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def allSteps(request):
    userid = request.user.id
    if (request.method == 'GET'):
        return HttpResponse("GET Request to All Steps")

    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        recipe = Recipe.objects.get(pk = body['recipe'])
        step = recipe.step_set.create(
                orderValue = body['orderValue'], 
                description = body['description'], 
                user_id = userid,
            )
            
        step.save()

        materialArray = body['materials']
        for material in materialArray:
            materialObject = Material.objects.get(pk = material['value'])
            materialObject.steps.add(step)
        
        return HttpResponse("POST Request to All Steps")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def stepById(request, id):
    userid = request.user.id
    if (request.method == 'GET'):
        return HttpResponse("GET Request to Step by ID")

    elif (request.method == 'PUT'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        step =  Step.objects.get(pk = id)
        valueid = step.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            step.orderValue = body['orderValue']
            step.description = body['description']
            step.material_set.clear()

            materialArray = body['materials']
            for material in materialArray:
                materialObject = Material.objects.get(pk = material['value'])
                materialObject.steps.add(step)
            
            step.save()
            return HttpResponse("PUT Request to Step by ID")

    elif (request.method == 'DELETE'):
        step = Step.objects.get(pk = id)
        valueid = step.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            step.delete()
            return HttpResponse("DELETE Request to Step by ID")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def allInventory(request):
    userid = request.user.id
    if (request.method == 'GET'):
        return HttpResponse("GET Request to All Inventory Items")

    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        material = Material.objects.get(pk = body['material'])
        inventory = material.inventory_set.create(
            lotNumber = body['lotNumber'], 
            expiryDate = body['expiryDate'],
            user_id = userid,
        )
        
        inventory.save()
        return HttpResponse("POST request successful")

    else:
        return HttpResponse("Error, not an allowed procedure")

@login_required
@csrf_protect
def inventoryById(request, id):
    userid = request.user.id
    if (request.method == 'GET'):
        return HttpResponse("GET Request to Inventory Item by ID")

    elif (request.method == 'PUT'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        inventory =  Inventory.objects.get(pk = id)
        valueid = inventory.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            inventory.lotNumber = body['lotNumber']
            inventory.expiryDate = body['expiryDate']
            inventory.save()
            return HttpResponse("PUT Request to Inventory Item by ID")

    elif (request.method == 'DELETE'):
        inventory = Inventory.objects.get(pk = id)
        valueid = inventory.user.id
        if (valueid != userid):
            return HttpResponseForbidden("You don't have acces to this item!")
        else:
            inventory.delete()
            return HttpResponse("DELETE Request to Inventory Item by ID")

    else:
        return HttpResponse("Error, not an allowed procedure")