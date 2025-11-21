from enum import Enum, auto

# NOTE: The custom AutoName mixin is generally required for Python versions < 3.11.
# If Python >= 3.11 is guaranteed, StrEnum can be used directly for a cleaner result.
# We will use the custom AutoName approach here for broader compatibility,
# but structure the code for maximum readability.

class AutoName(Enum):
    """
    Mixin class that automatically assigns the member's name as its value.
    This ensures that TransferType.MAIN_C2C.value == 'MAIN_C2C'.
    """
    def _generate_next_value_(name, start, count, last_values):
        return name


class TransferType(AutoName):
    """
    Defines the available asset transfer directions between different exchange accounts.
    The format is generally SOURCE_DESTINATION.
    """

    # =======================================================
    # MAIN (Spot/Master Wallet) as Source
    # = =====================================================
    MAIN_C2C = auto()           # To C2C Account
    MAIN_UMFUTURE = auto()      # To USDⓈ-M Futures Account
    MAIN_CMFUTURE = auto()      # To COIN-M Futures Account
    MAIN_MARGIN = auto()        # To Cross Margin Account
    MAIN_MINING = auto()        # To Mining Account

    # =======================================================
    # C2C (Peer-to-Peer) as Source
    # = =====================================================
    C2C_MAIN = auto()           # To Spot Account
    C2C_UMFUTURE = auto()       # To USDⓈ-M Futures Account
    C2C_MINING = auto()         # To Mining Account
    C2C_MARGIN = auto()         # To Cross Margin Account

    # =======================================================
    # UMFUTURE (USDⓈ-M Futures) as Source
    # = =====================================================
    UMFUTURE_MAIN = auto()      # To Spot Account
    UMFUTURE_C2C = auto()       # To C2C Account
    UMFUTURE_MARGIN = auto()    # To Cross Margin Account

    # =======================================================
    # CMFUTURE (COIN-M Futures) as Source
    # = =====================================================
    CMFUTURE_MAIN = auto()      # To Spot Account
    CMFUTURE_MARGIN = auto()    # To Cross Margin Account

    # =======================================================
    # MARGIN (Cross Margin) as Source
    # = =====================================================
    MARGIN_MAIN = auto()        # To Spot Account
    MARGIN_UMFUTURE = auto()    # To USDⓈ-M Futures Account
    MARGIN_CMFUTURE = auto()    # To COIN-M Futures Account
    MARGIN_MINING = auto()      # To Mining Account
    MARGIN_C2C = auto()         # To C2C Account

    # =======================================================
    # MINING (Mining Pool) as Source
    # = =====================================================
    MINING_MAIN = auto()        # To Spot Account
    MINING_UMFUTURE = auto()    # To USDⓈ-M Futures Account
    MINING_C2C = auto()         # To C2C Account
    MINING_MARGIN = auto()      # To Cross Margin Account
