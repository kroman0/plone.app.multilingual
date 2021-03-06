from zope.app.publisher.interfaces.browser import IBrowserMenu
from zope.app.publisher.interfaces.browser import IBrowserSubMenuItem
from zope import interface
from zope import schema
from plone.app.multilingual import _
from plone.app.multilingual.browser.vocabularies import (
    untranslated_languages,
    deletable_languages,
)
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.directives import form
from z3c.relationfield.schema import RelationChoice


class IMultilingualLayer(interface.Interface):
    """ browser layer """


class ITranslateSubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the translate menu.
    """


class ITranslateMenu(IBrowserMenu):
    """The translate menu.
    """


class ICreateTranslation(interface.Interface):

    language = schema.Choice(
        title=_(u"title_language", default=u"Language"),
        source=untranslated_languages,
    )


class IAddTranslation(form.Schema):

    language = schema.Choice(
        title=_(u"title_language", default=u"Language"),
        source=untranslated_languages,
        required=True,
    )
    content = RelationChoice(
        title=_(u"content"),
        source=ObjPathSourceBinder({'language': 'all'}),
        required=True,
    )


class IRemoveTranslation(form.Schema):

    languages = schema.List(
        title=_(u"title_languages"),
        value_type=schema.Choice(
            title=_(u"title_language", default=u"Language"),
            source=deletable_languages,
        ),
        required=True,
    )
    form.widget(languages='z3c.form.browser.select.SelectFieldWidget')

interface.alsoProvides(IAddTranslation, form.IFormFieldProvider)
interface.alsoProvides(IRemoveTranslation, form.IFormFieldProvider)
