#
#
#
# class UserPost(blocks.StructBlock):
#     first_name = blocks.CharBlock()
#     surname = blocks.CharBlock()
#     photo = ImageChooserBlock(required=False)
#     biography = blocks.RichTextBlock()
#
#     content_panels = Page.content_panels + [
#         FieldPanel('first_name'),
#         FieldPanel('surname'),
#         FieldPanel('biography', classname="full"),
#     ]
#
#     class Meta:
#         template = 'person/user_post.html'
#         icon = 'user'