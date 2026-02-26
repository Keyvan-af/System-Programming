## **User Mode vs Kernel Mode: Key Differences**

### **User Mode**
- **Purpose**: Runs user applications (browsers, games, text editors)
- **Access Level**: Restricted access to hardware and memory
- **Memory Access**: Can only access its own assigned memory space
- **Privilege**: Lower privilege level
- **System Communication**: Must use **System Calls** to request services from the kernel
- **Examples**: Chrome, Microsoft Word, Spotify

### **Kernel Mode**
- **Purpose**: Runs the operating system core components
- **Access Level**: Full, unrestricted access to hardware and all system memory
- **Memory Access**: Can access any memory location
- **Privilege**: Highest privilege level
- **System Communication**: Direct access to all system resources
- **Examples**: Device drivers, memory manager, process scheduler

---

## **What Happens When a Crash Occurs?**

### **🔹 Crash in User Mode**
- **Impact**: Isolated to the specific application
- **System Status**: Operating system continues running normally
- **User Experience**: 
  - Application closes unexpectedly
  - Error message like "App has stopped working" appears
  - Other applications remain unaffected
  - No system restart needed
- **Example**: When Microsoft Word crashes, you can still browse the internet

### **🔸 Crash in Kernel Mode**
- **Impact**: Affects the entire system
- **System Status**: Operating system becomes unstable or completely stops
- **User Experience**:
  - **Windows**: Blue Screen of Death (BSOD) appears
  - **Linux/macOS**: Kernel Panic message displayed
  - All running applications freeze and stop working
  - System typically needs to restart
- **Example**: A faulty graphics driver crashes → entire computer freezes and shows BSOD
