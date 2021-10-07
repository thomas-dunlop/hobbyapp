from django.urls import path

from . import views

app_name = 'dataretrievalapi'
urlpatterns = [
    path('project', views.allProjects, name='allProjects'),
    path('project/<int:id>', views.projectById, name='projectById'),
    path('recipe', views.allRecipes, name='allRecipes'),
    path('recipe/<int:id>', views.recipeById, name='recipeById'),
    path('material', views.allMaterials, name='allMaterials'),
    path('material/<int:id>', views.materialById, name='materialById'),
    path('step', views.allSteps, name='allSteps'),
    path('step/<int:id>', views.stepById, name='stepById'),
    path('inventory', views.allInventory, name='allInventory'),
    path('inventory/<int:id>', views.inventoryById, name='inventoryById'),
    path('userinfo', views.getUserInfo, name='userinfo'),
]