from .models import Project, Recipe, Material
import json
from django.db import connection

# Helper functions 
# def getAllRelated(parentLookUp, parents, children):
#     parentList = []
#     counter = 0
#     for parent in parentLookUp:
#         parentInfo = parents[counter]
#         for child in children:

def getProjectsByMaterial(materialId):
    with connection.cursor() as cursor:
        cursor.execute("WITH recipeToProjectTable AS (WITH stepToRecipeTable AS (WITH materialToStepTable AS (SELECT dataretrievalapi_material_steps.material_id, dataretrievalapi_step.recipe_id FROM dataretrievalapi_material_steps INNER JOIN dataretrievalapi_step ON dataretrievalapi_step.id = dataretrievalapi_material_steps.step_id) SELECT DISTINCT materialToStepTable.material_id, dataretrievalapi_recipe.id FROM materialToStepTable INNER JOIN dataretrievalapi_recipe ON materialToStepTable.recipe_id = dataretrievalapi_recipe.id) SELECT stepToRecipeTable.material_id, dataretrievalapi_recipe_projects.project_id FROM stepToRecipeTable INNER JOIN dataretrievalapi_recipe_projects ON stepToRecipeTable.id = dataretrievalapi_recipe_projects.recipe_id) SELECT * FROM recipeToProjectTable INNER JOIN dataretrievalapi_project ON recipeToProjectTable.project_id = dataretrievalapi_project.id WHERE recipeToProjectTable.material_id = %s", [materialId])
        rows = dictfetchall(cursor)
    return rows

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# Database search functions
def getAllProjects(userid):
    projects = Project.objects.all().filter(user_id = userid).values()
    projectsJson = json.dumps(list(projects))
    return projectsJson

def getProjectById(id):
    lookUpProject = Project.objects.get(pk = id)
    project = Project.objects.values().get(pk = id)

    recipes = list(lookUpProject.recipe_set.all().values())
    lookUpRecipes = lookUpProject.recipe_set.all()
    recipeList = []
    counter = 0
    for recipe in lookUpRecipes:
        recipeInfo = recipes[counter]
        
        projects = list(recipe.projects.all().values())
        steps = list(recipe.step_set.all().values())
        lookUpSteps = recipe.step_set.all()
        counter2 = 0
        stepList = []
        for step in lookUpSteps:
            stepInfo = steps[counter2]
            materials = list(step.material_set.all().values())
            stepList.append({"step": stepInfo, "materials": materials})
            counter2 += 1

        recipeList.append({"recipe": recipeInfo, "steps": stepList, "projects": projects})
        counter += 1

    data = json.dumps([{"project": project, "recipes": recipeList}])
    return data

def getAllRecipes(userid):
    recipes = Recipe.objects.all().filter(user_id = userid).values()
    lookUpRecipes = Recipe.objects.filter(user_id = userid).all()
    recipeList = []
    counter = 0
    for recipe in lookUpRecipes:
        recipeInfo = recipes[counter]

        projects = list(recipe.projects.all().values())
        steps = list(recipe.step_set.all().values())
        lookUpSteps = recipe.step_set.all()
        counter2 = 0
        stepList = []
        for step in lookUpSteps:
            stepInfo = steps[counter2]
            materials = list(step.material_set.all().values())
            stepList.append({"step": stepInfo, "materials": materials})
            counter2 += 1

        recipeList.append({"recipe": recipeInfo, "steps": stepList, "projects": projects})
        counter += 1


    recipesJson = json.dumps(recipeList)
    return recipesJson

def getAllMaterials(userid):
    categories = list(Material.objects.filter(user_id = userid).order_by('category').distinct('category').values('category'))
    categoryList = []
    for category in categories:
        materials = list(Material.objects.filter(category = category["category"], user_id = userid).values())
        lookUpMaterials = Material.objects.filter(category = category["category"], user_id = userid)
        counter = 0
        materialList = []
        for material in lookUpMaterials:
            materialInfo = materials[counter]
            inventoryItems = list(material.inventory_set.all().values())
        
            projects = getProjectsByMaterial(material.id)

            materialList.append({"material": materialInfo, "inventory": inventoryItems, "projects": projects})
            counter += 1
        categoryList.append({"category": category["category"], "materials": materialList})

    return json.dumps(categoryList, default=str)
