from Products.CMFCore.utils import getToolByName

def uninstall(self, reinstall=False):
    if not reinstall:
        setup_tool = getToolByName(self, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile('profile-qi.jabberHelpdesk:uninstall')
        registry = setup_tool.getImportStepRegistry()
        qijhSteps = [a['id'] for a in registry.listStepMetadata() if 'qi.jabberHelpdesk' in a['handler']]
        for step in qijhSteps:
            registry.unregisterStep(step)

