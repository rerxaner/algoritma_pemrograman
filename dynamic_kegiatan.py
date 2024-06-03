def min_time_to_complete_chores(chores, times):
    # chores adalah daftar tugas
    # times adalah daftar waktu yang dibutuhkan untuk setiap tugas

    n = len(chores)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + times[i - 1]

    completed_chores = []
    for i in range(n):
        completed_chores.append(chores[i])
        print(f"Menyelesaikan: {chores[i]} dalam waktu {times[i]}")

    return dp[n], completed_chores

chores = ['Mencuci piring', 'Menyapu lantai', 'Mencuci baju', 'Mengelap meja']
times = [10, 15, 30, 5]  # waktu dalam menit untuk setiap tugas

total_time, completed = min_time_to_complete_chores(chores, times)
print(f"Waktu total yang diperlukan: {total_time} menit")
print(f"Pekerjaan yang telah selesai: {completed}")
