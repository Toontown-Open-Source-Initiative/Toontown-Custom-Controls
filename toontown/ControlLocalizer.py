ControlSettingsTitle = 'Control Settings'
ControlSettingsInfoLabelDefault = 'Change your input settings here.'
ControlSettingsInfoLabelChangeKey = 'Press a key combination\ncreate your new hotkey.'
ControlSettingsAlreadyInUse = 'That key combination is already\nin use. Please choose another.'
ControlSettingsSuccessful = 'Hotkey set successfully.'
ControlSettingsChangesApplied = 'All changes applied successfully.'

# Below is an example of how to convert a string to include the proper name of a hotkey.
# For example, here is the original Ice Slide game instructions:

IceGameInstructions = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points and avoid the TNT!'

# This is the updated version:

IceGameInstructions = 'Get as close to the center by the end of the second round. Use movement keys to change direction and force. Press  %0004 to launch your toon.  Hit barrels for extra points and avoid the TNT!'

# You should replace all instances of "arrow keys", "left and right keys", etc. with "movement keys" to keep everything consistent.
# Replace specific hotkey names such as "Ctrl" with a special ID. This ID will be formatted using a function in the ControlManager.
# Typically, you can format the string like so:

base.controlManager.convertHotkeyString(TTLocalizer.IceGameInstructionsNoTnt, '%')

# The last argument is the identififer you're using. Most of the time you'll want to use a $ instead of a % like in the example above.
# Make sure to put TWO spaces in between the identifier and the previous word.
