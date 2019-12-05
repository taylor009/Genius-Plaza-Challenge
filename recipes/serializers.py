from rest_framework import serializers
from recipes.models import Recipe, Step, Ingredient


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    steps = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        # Query recipe object
        fields = ('owner', 'name', 'steps', 'ingredients', 'url')


class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'step_text', 'recipe', 'url')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'text', 'recipe', 'url')
