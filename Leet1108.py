
class Leet1108:

    def defang_ip_address(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == "__main__":
    defanger = Leet1108()
    address = '255.555.55.0'
    print(defanger.defang_ip_address(address))