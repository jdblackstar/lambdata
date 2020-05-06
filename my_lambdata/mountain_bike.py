class MountainBike():
    """
    MountainBike class

    Attributes:
    - wheel_size: int (27.5, 29)
    - suspension: str ('full', 'soft', 'hard')
    - brand: str ('Specialized', 'Trek', 'Yeti')

    Methods:
    - wheelie (property)
    - jump (property)
    - crash (static)

    """
    
    def __init__(self, wheel_size, suspension, brand):
        self.wheel_size = wheel_size
        self.suspension = suspension
        self.brand = brand

    @property
    def wheelie(self):
        if self.wheel_size == 27.5:
            print(f'Bikes with {self.wheel_size} in wheels were made for wheelies!')
        elif self.wheel_size == 29:
            print(f"If you can wheelie on a {self.wheel_size}er, you're a God")
        else:
            return
            
    @property
    def jump(self):
        if self.suspension == "full":
            print(f'Jumps are easy for a bike with {self.suspension} suspension!')
        elif self.suspension == 'soft':
            print(f'This could hurt a little bit...')
        elif self.suspension == 'hard':
            print(f"Don't even try it, brother.")
        else:
            return


    @staticmethod
    def crash():
        print(f'Ouch...')


if __name__ == "__main__":

    bike1 = MountainBike(wheel_size=27.5, suspension='soft', brand='Trek')
    print(bike1.wheel_size, bike1.suspension, bike1.brand)
    bike1.wheelie

    bike2 = MountainBike(wheel_size=29, suspension='full', brand='Specialized')
    print(bike2.wheel_size, bike2.suspension, bike2.brand)
    bike2.jump

    bike3 = MountainBike(wheel_size=29, suspension='hard', brand='Yeti')
    print(bike3.wheel_size, bike3.suspension, bike3.brand)
    bike3.crash