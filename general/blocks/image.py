from django import forms

from wagtail.wagtailcore.blocks import FieldBlock, StructBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(
        choices=(
            ('img-fluid', 'Image fluid'),
            ('img-fluid full-width', 'Full width'),
        )
    )


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    alignment = ImageFormatChoiceBlock()

    class Meta:
        template = 'general/blocks/image.html'
        icon = "image"
