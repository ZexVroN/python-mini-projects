all_contact = []
cek = False

while cek == False:
    print("=== CONTACT MANAGER ====")
    print("1. Add contact")
    print("2. Show contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    input_user = int(input("Choose menu : "))

    if input_user == 1:
        data_nama = str(input("Masukan Nama = "))
        data_nomor_telepon = str(input("Masukan No = "))
        data_email = str(input("Masukan Email = "))

        contact = {
            "Nama": data_nama,
            "No Telepon": data_nomor_telepon,
            "Email": data_email,
        }

        all_contact.append(contact)

    elif input_user == 2:
        for kon in all_contact:
            print("=== CONTACT ===")
            print(f"Nama = {kon['Nama']}")
            print(f"No Telepon = {kon['No Telepon']}")
            print(f"Email = {kon['Email']}")

    elif input_user == 3:
        print("Search contact by \n 1. Index \n 2. Nama")
        pilihan = int(input("Masukan pilihan = "))
        if pilihan == 1:
            index_pilihan = int(input("Masukan index = "))
            print("=== CONTACT ===")
            print(f"Nama = {all_contact[index_pilihan]['Nama']}")
            print(f"No Telepon = {all_contact[index_pilihan]['No Telepon']}")
            print(f"Email = {all_contact[index_pilihan]['Email']}")
        elif pilihan == 2:
            cek_pilihan = False
            nama_pilihan = input("Masukan nama = ")
            for kon in all_contact:
                if nama_pilihan == kon["Nama"]:
                    print("=== CONTACT ===")
                    print(f"Nama = {kon['Nama']}")
                    print(f"No Telepon = {kon['No Telepon']}")
                    print(f"Email = {kon['Email']}")
                    cek_pilihan = True

            if cek_pilihan == False:
                print(nama_pilihan, "Tidak ditemukan")

    elif input_user == 4:
        print("Remove contact by \n 1. Index \n 2. Nama")
        pilihan = int(input("Masukan pilihan = "))
        if pilihan == 1:
            index_pilihan = int(input("Masukan index yang ingin dihapus = "))
            if index_pilihan >= 0 and index_pilihan < len(all_contact):
                del all_contact[index_pilihan]
                print(f"Contact dengan index -{index_pilihan} berhasil dihapus!")
            else:
                print(f"Data dengan index -{index_pilihan} tidak ditemukan")

        elif pilihan == 2:
            cek_nama_pilihan = False
            nama_pilihan = input("Masukan nama yang ingin dihapus = ")
            for kon in all_contact:
                if nama_pilihan == kon['Nama'] :
                    all_contact.remove(kon)
                    cek_nama_pilihan = True

            if cek_nama_pilihan :
                print("Nama pilihan berhasil dihapus")
            else :
                print("Kontak tidak ditemukan")

    elif input_user == 5:
        input_pengguna = input("Do you wanna quit? IF YES INPUT 'Y'")
        if input_pengguna == "Y":
            print("Berhasil keluar")
            break