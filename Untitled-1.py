import time

# 1. Dekorator funksiyasi
def vaqt_olchovchi(asosiy_funksiya):
    def qobiq(*args, **kwargs):
        boshlanish = time.time()
        
        # Asosiy funksiya ishga tushadi
        natija = asosiy_funksiya(*args, **kwargs)
        
        tugash = time.time()
        print(f"[{asosiy_funksiya.__name__}] funksiyasi {tugash - boshlanish:.4f} soniya ishladi.")
        return natija
    return qobiq

# 2. Dekoratordan foydalanish:
@vaqt_olchovchi
def ogir_hisob_kitob():
    time.sleep(1) # 1 soniya kutish
    return "Hisob-kitob tayyor!"

print(ogir_hisob_kitob())