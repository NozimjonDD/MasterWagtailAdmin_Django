from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core import blocks
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    phone = models.IntegerField(default=99899000112)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('phone', ),
    ]

    # template = 'blogs/blog_index.html'


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    # template = 'blogs/blog_page.html'
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images")
    ]

    def get_context(self, request, *args):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpage_children'] = blogpages
        return context


class ChildBlogPage(Page):
    created_at = models.DateField("Post date")
    img = models.ForeignKey('wagtailimages.Image',
                            null=True,
                            blank=True,
                            on_delete=models.PROTECT,
                            related_name='+'
                            )
    description = models.TextField(blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('created_at'),
        ImageChooserPanel('img'),
        FieldPanel('description')
    ]


class BlogPageGalleryImage(Orderable):
    text = models.TextField()
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('text'),
    ]


class UserPost(blocks.StructBlock):
    first_name = blocks.CharBlock()
    surname = blocks.CharBlock()
    photo = ImageChooserBlock(required=False)
    biography = blocks.RichTextBlock()

    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('surname'),
        FieldPanel('biography', classname="full"),
    ]

    class Meta:
        template = 'person/user_post.html'
        icon = 'user'
