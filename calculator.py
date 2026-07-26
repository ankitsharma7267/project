import tkinter as tk
from tkinter import ttk
import math

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#1e1e1e')
        
        # Variables
        self.current = ""
        self.result = ""
        self.history = []
        
        # Configure styles
        self.setup_styles()
        
        # Create main container
        main_frame = tk.Frame(root, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top section with displays
        top_frame = tk.Frame(main_frame, bg='#1e1e1e')
        top_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Left side - Main display
        left_display_frame = tk.Frame(top_frame, bg='#1e1e1e')
        left_display_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Main display (expression)
        self.expr_display = tk.Entry(left_display_frame, 
                                     font=('Segoe UI', 16), 
                                     bg='#2b2b2b', 
                                     fg='#ffffff',
                                     borderwidth=0,
                                     justify=tk.RIGHT,
                                     insertbackground='#ffffff')
        self.expr_display.pack(fill=tk.X, ipady=10, padx=(0, 10))
        
        # Result display
        self.result_display = tk.Label(left_display_frame, 
                                       text="0", 
                                       font=('Segoe UI', 24, 'bold'),
                                       bg='#2b2b2b', 
                                       fg='#4CAF50',
                                       anchor='e',
                                       padx=10,
                                       pady=5)
        self.result_display.pack(fill=tk.X, padx=(0, 10), pady=(5, 0))
        
        # Right side - History display
        history_frame = tk.Frame(top_frame, bg='#2b2b2b', width=150)
        history_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 0))
        history_frame.pack_propagate(False)
        
        # History label
        history_label = tk.Label(history_frame, 
                                text="History", 
                                font=('Segoe UI', 10, 'bold'),
                                bg='#2b2b2b', 
                                fg='#888888')
        history_label.pack(pady=(5, 0))
        
        # History listbox with scrollbar
        history_container = tk.Frame(history_frame, bg='#2b2b2b')
        history_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(history_container, bg='#2b2b2b')
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_listbox = tk.Listbox(history_container,
                                          bg='#2b2b2b',
                                          fg='#cccccc',
                                          font=('Segoe UI', 9),
                                          borderwidth=0,
                                          highlightthickness=0,
                                          selectbackground='#3a3a3a',
                                          yscrollcommand=scrollbar.set)
        self.history_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.history_listbox.yview)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg='#1e1e1e')
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Define buttons
        buttons = [
            ['C', 'CE', '⌫', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
            ['√', 'x²', '(', ')']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            row_frame = tk.Frame(button_frame, bg='#1e1e1e')
            row_frame.pack(fill=tk.BOTH, expand=True, pady=2)
            
            for j, text in enumerate(row):
                btn = self.create_button(row_frame, text)
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
        
        # Bind keyboard events
        self.bind_keys()
        
    def setup_styles(self):
        """Configure button styles"""
        style = ttk.Style()
        style.theme_use('default')
        
    def create_button(self, parent, text):
        """Create a styled button"""
        # Determine button color based on type
        if text in ['=']:
            bg = '#4CAF50'
            hover_bg = '#5CBF60'
            fg = '#ffffff'
        elif text in ['C', 'CE', '⌫']:
            bg = '#f44336'
            hover_bg = '#ff5544'
            fg = '#ffffff'
        elif text in ['÷', '×', '-', '+', '√', 'x²', '(', ')']:
            bg = '#FF9800'
            hover_bg = '#FFa820'
            fg = '#ffffff'
        else:
            bg = '#424242'
            hover_bg = '#535353'
            fg = '#ffffff'
        
        btn = tk.Button(parent, 
                       text=text,
                       font=('Segoe UI', 14, 'bold'),
                       bg=bg,
                       fg=fg,
                       borderwidth=0,
                       padx=20,
                       pady=20,
                       activebackground=hover_bg,
                       activeforeground=fg,
                       command=lambda t=text: self.button_click(t))
        
        # Bind hover effects
        btn.bind('<Enter>', lambda e, b=btn, h=hover_bg: b.config(bg=h))
        btn.bind('<Leave>', lambda e, b=btn, n=bg: b.config(bg=n))
        
        return btn
    
    def button_click(self, value):
        """Handle button clicks"""
        if value == 'C':
            self.clear_all()
        elif value == 'CE':
            self.clear_entry()
        elif value == '⌫':
            self.backspace()
        elif value == '=':
            self.calculate()
        elif value == '±':
            self.toggle_sign()
        elif value == '√':
            self.square_root()
        elif value == 'x²':
            self.square()
        elif value == '÷':
            self.add_to_expression('/')
        elif value == '×':
            self.add_to_expression('*')
        else:
            self.add_to_expression(value)
    
    def add_to_expression(self, value):
        """Add value to current expression"""
        self.current += str(value)
        self.update_display()
    
    def update_display(self):
        """Update the expression display"""
        self.expr_display.delete(0, tk.END)
        self.expr_display.insert(0, self.current)
        
        # Try to evaluate and show preview
        try:
            if self.current:
                result = eval(self.current)
                self.result_display.config(text=f"= {result}")
        except:
            self.result_display.config(text="= 0")
    
    def calculate(self):
        """Calculate the result"""
        try:
            if self.current:
                result = eval(self.current)
                # Add to history
                self.add_to_history(f"{self.current} = {result}")
                # Update displays
                self.current = str(result)
                self.update_display()
                self.result_display.config(text=f"= {result}")
        except Exception as e:
            self.result_display.config(text="Error")
            self.current = ""
            self.update_display()
    
    def clear_all(self):
        """Clear everything"""
        self.current = ""
        self.update_display()
        self.result_display.config(text="0")
    
    def clear_entry(self):
        """Clear current entry"""
        self.current = ""
        self.update_display()
    
    def backspace(self):
        """Remove last character"""
        self.current = self.current[:-1]
        self.update_display()
    
    def toggle_sign(self):
        """Toggle positive/negative"""
        try:
            if self.current:
                value = eval(self.current)
                self.current = str(-value)
                self.update_display()
        except:
            pass
    
    def square_root(self):
        """Calculate square root"""
        try:
            if self.current:
                value = eval(self.current)
                result = math.sqrt(value)
                self.add_to_history(f"√{value} = {result}")
                self.current = str(result)
                self.update_display()
        except:
            self.result_display.config(text="Error")
    
    def square(self):
        """Calculate square"""
        try:
            if self.current:
                value = eval(self.current)
                result = value ** 2
                self.add_to_history(f"{value}² = {result}")
                self.current = str(result)
                self.update_display()
        except:
            self.result_display.config(text="Error")
    
    def add_to_history(self, entry):
        """Add calculation to history"""
        self.history_listbox.insert(0, entry)
        # Keep only last 20 entries
        if self.history_listbox.size() > 20:
            self.history_listbox.delete(20)
    
    def bind_keys(self):
        """Bind keyboard shortcuts"""
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<KP_Enter>', lambda e: self.calculate())
        self.root.bind('<BackSpace>', lambda e: self.backspace())
        self.root.bind('<Escape>', lambda e: self.clear_all())
        
        # Bind number keys
        for i in range(10):
            self.root.bind(str(i), lambda e, n=i: self.add_to_expression(str(n)))
        
        # Bind operators
        self.root.bind('+', lambda e: self.add_to_expression('+'))
        self.root.bind('-', lambda e: self.add_to_expression('-'))
        self.root.bind('*', lambda e: self.add_to_expression('*'))
        self.root.bind('/', lambda e: self.add_to_expression('/'))
        self.root.bind('.', lambda e: self.add_to_expression('.'))
        self.root.bind('(', lambda e: self.add_to_expression('('))
        self.root.bind(')', lambda e: self.add_to_expression(')'))

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()