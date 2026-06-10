
from tkinter import *
import socket
import threading
import time 
from tkinter import ttk

COMMON_PORTS = {20:"FTP Data", 21:"FTP Control", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS", 80:"HTTP", 110:"POP3", 143:"IMAP", 443:"HTTPS", 3306:"MySQL", 3389:"RDP", 5900:"VNC", 6379:"Redis", 8080:"HTTP-Alt"}
root = Tk()
root.configure(
    bg="black"
)
root.title("CyberScan v2")
root.geometry("700x500")

progress = ttk.Progressbar(
    root,
    length=300,
    mode="determinate"
)
progress.pack()
def scan_port(target_ip, port):

    s = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    s.settimeout(0.5)

    conn = s.connect_ex(
        (target_ip, port)
    )

    if conn == 0:
        service = COMMON_PORTS.get(port, "Unknown Service")
        results_box.insert( END, f"Port {port} OPEN ({service})\n" )
    s.close()

progress["value"] = 0
def run_scan():
    
    progress["value"] = 0
    target = target_entry.get()

    try:

        start_port = int(
            start_entry.get()
        )

        end_port = int(
            end_entry.get()
        )

        target_ip = socket.gethostbyname(
            target
        )

    except ValueError:

        status_label.config(
            text="Invalid Port Number"
        )

        return

    except socket.gaierror:

        status_label.config(
            text="Invalid Hostname"
        )

        return

    results_box.delete(
        "1.0",
        END
    )

    results_box.insert(
        END,
        f"Target: {target}\n"
    )

    results_box.insert(
        END,
        f"Resolved IP: {target_ip}\n"
    )

    results_box.insert(
        END,
        f"Port Range: {start_port}-{end_port}\n\n"
    )
    status_label.config(
        text="Scanning...",
        fg="orange"
    )
    scan_start_time = time.time()
    total_ports = (
    end_port
    - start_port
    + 1
)

    current_port_count = 0
    for port in range(
        start_port,
        end_port + 1
    ):
        scan_port(
            target_ip,
            port
        )
        current_port_count += 1
        progress['value'] = (current_port_count / total_ports) * 100
        root.update_idletasks()
    scan_end_time = time.time()
    scan_duration = scan_end_time - scan_start_time
    results_box.insert(
    END,
    f"\nScan completed in {scan_duration:.2f} seconds\n"
)
    status_label.config(
        text="Scan Complete",
        fg="#00ff88"
    )


def start_scan():

    thread = threading.Thread(
        target=run_scan
    )

    thread.daemon = True
    thread.start()


title_label = Label(
    root,
    text="CyberScan v2",
    font=("Consolas", 24, "bold"),
    bg="#1e1e1e",
    fg="#00ff88",
    borderwidth=2,
    relief="solid"
)

title_label.pack(
    pady=15
)

target_label = Label(
    root,
    text="Target",
    bg="#1e1e1e",
    fg="white"
)

target_label.pack()

target_entry = Entry(
    root,
     width=40,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

target_entry.pack(
    pady=5
)

start_label = Label(
    root,
    text="Start Port",
     bg="#1e1e1e",
    fg="white"
)

start_label.pack()

start_entry = Entry(
    root,
    width=40
)

start_entry.pack(
    pady=5
)

end_label = Label(
    root,
    text="End Port",
    bg="#1e1e1e",
    fg="white"
)

end_label.pack()

end_entry = Entry(
    root,
    width=40
)

end_entry.pack(
    pady=5
)

scan_button = Button(
    root,
  text="Start Scan",
    command=start_scan,
    bg="#00aa55",
    fg="white",
    font=("Consolas", 11, "bold")
)

scan_button.pack(
    pady=15
)

status_label = Label(
    root,
    text="Ready",
    font=("Arial", 12)
)

status_label.pack(
    pady=10
)

results_box = Text(
    root,
   height=15,
    width=80,
    bg="#121212",
    fg="#00ff88",
    insertbackground="white"
)

results_box.pack(
    pady=10
)

root.mainloop()
