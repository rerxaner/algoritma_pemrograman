def household_chores(chores):
    # ! chores adalah daftar tugas tugas yang perlu di lakukan
    completed_chores = []
    for chore in chores:
        completed_chores.append(chore)
        print(f"Meyelesaikan: {chore}")
    return completed_chores

chores = ['Mencuci piring','Meyapu lantai','Mencuci baju','Mengelap meja']
completed = household_chores(chores)
print(f"Perkerjaan yang telah selesai: {completed}")