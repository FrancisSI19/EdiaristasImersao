from django.urls import path
from administracao.views.servico_views import *    
from administracao.views.usuario_views import *
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy    

urlpatterns = [
    path('servicos/cadastrar', cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', editar_servico, name='editar_servico'),
    path('usuarios/cadastrar', cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar', listar_usuarios, name='listar_usuarios'),
    path('usuarios/editar/<int:id>', editar_usuarios, name='editar_usuario'),
    path('autenticacao/login', auth_views.LoginView.as_view(), name='logar_usuario'),
    path('autenticacao/logout', auth_views.LogoutView.as_view(), name='deslogar_usuario'),
    path('alterar_senha', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('listar_servicos')), name='alterar_senha'),
    path('resetar_senha', auth_views.PasswordResetView.as_view(), name='resetar_senha'),
    path('resetar_senha/sucesso', auth_views.PasswordResetDoneView.as_view(),
        name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uidb64><str:token>', auth_views.PasswordResetConfirmView.as_view(),
        name='resetar_senha_confirmar'),
    path('resetar_senha/feito', auth_views.PasswordResetDoneView.as_view(),
        name='resetar_senha_feito'),

]
