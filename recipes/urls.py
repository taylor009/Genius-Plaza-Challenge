from rest_framework import routers
from .views import RecipeViewSet, StepViewSet, IngredientViewSet

router = routers.DefaultRouter()

router.register('recipes', RecipeViewSet, 'recipes')
router.register('step', StepViewSet, 'steps')
router.register('ingredients', IngredientViewSet, 'ingredients')

urlpatterns = router.urls
