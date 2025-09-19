# store/admin.py
from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name'] # Adicionando campo de busca

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'is_special', 'created', 'updated']
    list_filter = ['available', 'is_special', 'created', 'updated']
    list_editable = ['price', 'available', 'is_special']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'get_total_price']
    list_editable = ['quantity']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'city', 'paid', 'created']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    # Opcional: Adicionar a seção de "Informações de Contato"
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações de Contato', {'fields': ('phone_number',)}),
    )
    # A list_display vai mostrar o novo campo na lista de usuários
    list_display = BaseUserAdmin.list_display + ('phone_number',)