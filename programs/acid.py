class AcidDosage:
    BASE_ACID_DROP = 100
    BASE_POOL_VOL = 40000
    PH_DROP_PER = 1.0

    def __init__(self, pool_volume_liters, current_ph, target_ph):
        self.pool_vol = pool_volume_liters
        self.current_ph = current_ph
        self.target_ph = target_ph

    def find_ph_drop(self):
        return self.current_ph - self.target_ph
    
    def find_acid_dose(self):
        ph_drop = self.find_ph_drop()
        return self.acid_volume_required(self.pool_vol, ph_drop)
    
    @classmethod
    def acid_volume_required(cls, pool_vol, ph_drop):
        #This uses the base rule of 100mL does 1 point per 40k
        return (ph_drop * cls.BASE_ACID_DROP * cls.BASE_POOL_VOL) / pool_vol
    
    @staticmethod
    def aarons_verdict():
        print("Use this before you make any phone calls. 100mL for 1 pt per 40k.")


if __name__ == "__main__":
    AcidDosage.aarons_verdict()

    volume = float(input("Pool volume: "))
    current_ph = float(input("Spin test result pH: "))
    target_ph = float(input("Ideal pH range (pick 1 value): "))
    #
    calculator = AcidDosage(volume, current_ph, target_ph)
    #
    dosage_needed = calculator.find_acid_dose()
    ##
    ##
    print(f"\nAdd {dosage_needed:.1f}mL of acid my bro.")
