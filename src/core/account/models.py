from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password as _make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def make_password(password):
    return _make_password(password)


class DTManager(BaseUserManager):
    use_in_migrates = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class DTAbstractBaseUser(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(_('password'), max_length=128)
    email = models.EmailField(_('email'), unique=True, max_length=150, error_messages={
        'unique': _("A user with that email already exists."),
    }, )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = DTManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True


class DTAbstractPreSignUpBaseUser(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=32, null=False)
    activation_code = models.CharField(max_length=36)
    password = models.CharField(_('password'), max_length=128, null=False)
    activated = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    @classmethod
    def _generate_verification_code(cls):
        NotImplementedError('Please implement in the subclass')

    def __str__(self):
        return "%s" % self.email

    @classmethod
    def presignup(cls, email, name, password):
        obj, is_created = cls.objects.update_or_create(
            email=email,
            name=name,
            verification_code=cls._generate_verification_code(),
            password=make_password(password),
        )
        return obj
