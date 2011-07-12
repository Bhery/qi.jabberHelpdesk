from Products.CMFCore.utils import getToolByName

def uninstallConfiglet(context):
    """ Remove the qi.jabberHelpdesk control panel item"""

    if context.readDataFile('uninstallConfiglet.txt') is None:
        return
    portal = context.getSite()
    cp = getToolByName(portal, 'portal_controlpanel')
    cp.unregisterApplication('qi.jabberHelpdesk')
    
