from PIL import Image
import os

def iegūt_kolāžas_nosaukumu(izvades_mape):
    while True:
        kolāžas_nosaukums = input("Ieraksti kolāžas nosaukumu: ")
        if not os.path.exists(os.path.join(izvades_mape, f"{kolāžas_nosaukums}.jpg")):
            return kolāžas_nosaukums
        else:
            print(f"Kolāža ar nosaukumu '{kolāžas_nosaukums}' jau eksistē, izvēlieties citu nosaukumu!")

attēlu_mape = "ievades bildes"
izvades_mape = "kolāžas bildes"
kolāžas_attēla_ceļš = os.path.join(izvades_mape, f"{iegūt_kolāžas_nosaukumu(izvades_mape)}.jpg")

def izveidot_foto_kolāžu(attēlu_mape, izvades_mape, atstarpe=10):
    attēlu_faili = [f for f in os.listdir(attēlu_mape) if f.endswith(('.jpg'))]
    num_kolonnas = 4 
    num_rindas = 2

    kolāžas_platums = 1660
    kolāžas_augstums = 1080

    attēla_rāmja_platums = (kolāžas_platums - (num_kolonnas + 1) * atstarpe) // num_kolonnas
    attēla_rāmja_augstums = (kolāžas_augstums - (num_rindas + 1) * atstarpe) // num_rindas

    novirze_x = (kolāžas_platums - (num_kolonnas * attēla_rāmja_platums + (num_kolonnas - 1) * atstarpe)) // 2
    novirze_y = (kolāžas_augstums - (num_rindas * attēla_rāmja_augstums + (num_rindas - 1) * atstarpe)) // 2

    kolāža = Image.new('RGB', (kolāžas_platums, kolāžas_augstums), (0, 0, 0))

    x, y = novirze_x, novirze_y

    for attēla_fails in attēlu_faili:
        attēla_ceļš = os.path.join(attēlu_mape, attēla_fails)
        img = Image.open(attēla_ceļš)

        img.thumbnail((attēla_rāmja_platums, attēla_rāmja_augstums))

        kolāža.paste(img, (x, y))

        x = x + attēla_rāmja_platums + atstarpe

        if x + attēla_rāmja_platums + atstarpe > kolāžas_platums:
            x = novirze_x
            y = y + attēla_rāmja_augstums + atstarpe
    kolāža.save(kolāžas_attēla_ceļš)

izveidot_foto_kolāžu(attēlu_mape, izvades_mape)
