# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 23:48
from __future__ import unicode_literals

from django.db import migrations
import general.blocks.card_List
import general.blocks.h1
import general.blocks.h2
import general.blocks.h3
import general.blocks.h4
import general.blocks.h5
import general.blocks.hr
import general.blocks.image
import general.blocks.markdown
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailsnippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h1', general.blocks.h1.H1Block()), ('h2', general.blocks.h2.H2Block()), ('h3', general.blocks.h3.H3Block()), ('h4', general.blocks.h4.H4Block()), ('h5', general.blocks.h5.H5Block()), ('hr', general.blocks.hr.HrBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('markdown', general.blocks.markdown.MarkDownBlock(rows=10)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', general.blocks.image.ImageFormatChoiceBlock())))), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('cite', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Paste your embed URL ie: https://www.youtube.com/watch?v=05GKqTZGRXU', icon='media')), ('page_link_cards', general.blocks.card_List.CardListBlock(wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('show_description', wagtail.wagtailcore.blocks.BooleanBlock(label='Show search description?', required=False)))))), ('custom_content', wagtail.wagtailsnippets.blocks.SnippetChooserBlock('general.CustomContent')))),
        ),
        migrations.AlterField(
            model_name='customcontent',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h1', general.blocks.h1.H1Block()), ('h2', general.blocks.h2.H2Block()), ('h3', general.blocks.h3.H3Block()), ('h4', general.blocks.h4.H4Block()), ('h5', general.blocks.h5.H5Block()), ('hr', general.blocks.hr.HrBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('markdown', general.blocks.markdown.MarkDownBlock(rows=10)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', general.blocks.image.ImageFormatChoiceBlock())))), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('cite', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Paste your embed URL ie: https://www.youtube.com/watch?v=05GKqTZGRXU', icon='media')), ('page_link_cards', general.blocks.card_List.CardListBlock(wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('show_description', wagtail.wagtailcore.blocks.BooleanBlock(label='Show search description?', required=False)))))))),
        ),
    ]