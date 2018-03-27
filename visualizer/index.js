const electron = require('electron');
const {app, BrowserWindow, Menu} = electron;

app.on('ready', () => {
    global.keepPriorGenerations = true;
    global.green = true;
    global.red = true;
    global.yellow = true;
    let win = new BrowserWindow({});
    let menu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(menu);
    win.loadURL(`file://${__dirname}/index.html`);
    win.maximize();
});

const menuTemplate = [
    {
        label: 'Application',
        submenu: [
            {
                role: 'reload'
            },
            {
                role: 'toggledevtools'
            },
            {
                role: 'quit'
            }
        ]
    },
    {
        label: 'Settings',
        submenu: [
            {
                label: 'Keep Prior Generations',
                type: 'checkbox',
                checked: true,
                click() {global.keepPriorGenerations = !global.keepPriorGenerations}
            },
            {
                label: 'Diffs',
                submenu: [
                    {
                        label: 'Show Correct Mutations',
                        sublabel: 'Will show correct mutations as green.',
                        type: 'checkbox',
                        checked: true,
                        click() {global.green = !global.green;}
                    },
                    {
                        label: 'Show Incorrect Mutations',
                        sublabel: 'Will show incorrect mutations as yellow.',
                        type: 'checkbox',
                        checked: true,
                        click() {global.yellow = !global.yellow}
                    },
                    {
                        label: 'Distinguish Divergent Mutations',
                        sublabel: 'If "Show Incorrect Mutations" is enabled, will show divergent mutations as red. If "Show Incorrect Mutations" is enabled and this isn\'t, divergent mutations will continue to show as yellow.',
                        type: 'checkbox',
                        checked: true,
                        click() {global.red = !global.red}
                    }
                ]
            }
        ]
    }
];

if(process.platform === 'darwin') {
    menuTemplate.unshift({});
}
