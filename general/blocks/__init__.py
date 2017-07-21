from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore import blocks
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from .card_List import CardListBlock
from .h1 import H1Block
from .h2 import H2Block
from .h3 import H3Block
from .h4 import H4Block
from .h5 import H5Block
from .hr import HrBlock
from .image import ImageBlock
from .markdown import MarkDownBlock
from .page_link import PageLinkCardBlock
from .quote import QuoteBlock


class CommonStreamBlock(blocks.StreamBlock):
    h1 = H1Block()
    h2 = H2Block()
    h3 = H3Block()
    h4 = H4Block()
    h5 = H5Block()
    hr = HrBlock()
    paragraph = blocks.RichTextBlock(icon='pilcrow')
    html = blocks.RawHTMLBlock()
    markdown = MarkDownBlock(rows=10)
    image = ImageBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")
    pullquote = QuoteBlock()
    embed = EmbedBlock(
        help_text=_('Paste your embed URL ie: https://www.youtube.com/watch?v=05GKqTZGRXU'),
        icon='media'
    )
    page_link_cards = CardListBlock(PageLinkCardBlock())


class GeneralStreamBlock(CommonStreamBlock):
    custom_content = SnippetChooserBlock('general.CustomContent')
