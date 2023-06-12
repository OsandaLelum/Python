import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        
        # Create a panel
        panel = wx.Panel(self)
        
        # Create a button
        button = wx.Button(panel, label="Click me")
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        
        # Create a sizer to arrange the button
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        
        # Set the sizer for the panel
        panel.SetSizer(sizer)
        
    def on_button_click(self, event):
        print("Button clicked!")

if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    
    # Create the main frame
    frame = MyFrame(None, "wxPython Example")
    
    # Show the frame
    frame.Show(True)
    
    # Start the wxPython event loop
    app.MainLoop()
