# SidebarFocus for Sublime Text 3

Simple package for focused on sidebar and unfocus when close sidebar.

### Installation

1. Install Package Controll
2. Install *SidebarFocus* from PackageControl

* You can change standart hotkey
```json
{ "keys": ["f1"], "command": "sidebar_focus" }
```

```json
// This option changes the behavior only when the sidebar is opened
// If true it'll close sidebar and focus back on the current file
// If false it'll reveal and focus the current file on sidebar
"close_sidebar_if_opened": true //by default
```


*If you like VIM navigation you can add for navigation in sidebar.*
```json
{
		"keys": ["h"],
		"command": "move",
		"args":
		{
			"by": "characters",
			"forward": false
		},
		"context":
		[
			{
				"key": "control",
				"operand": "sidebar_tree"
			}
		]
	},
	{
		"keys": ["j"],
		"command": "move",
		"args":
		{
			"by": "lines",
			"forward": true
		},
		"context":
		[
			{
				"key": "control",
				"operand": "sidebar_tree"
			}
		]
	},
	{
		"keys": ["k"],
		"command": "move",
		"args":
		{
			"by": "lines",
			"forward": false
		},
		"context":
		[
			{
				"key": "control",
				"operand": "sidebar_tree"
			}
		]
	},
	{
		"keys": ["l"],
		"command": "move",
		"args":
		{
			"by": "characters",
			"forward": true
		},
		"context":
		[
			{
				"key": "control",
				"operand": "sidebar_tree"
			}
		]
	},
```


Enjoy!
