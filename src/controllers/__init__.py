REGISTRY = {}

from .basic_controller import BasicMAC
from .non_shared_controller import NonSharedMAC
from .maddpg_controller import MADDPGMAC
from .group_controller import NMAC as GroupMAC
from .gacg_controller import GroupMessageMAC
from .ltscg_controller import LTSCG_GraphMAC

REGISTRY["basic_mac"] = BasicMAC
REGISTRY["non_shared_mac"] = NonSharedMAC
REGISTRY["maddpg_mac"] = MADDPGMAC
REGISTRY["group_mac"] = GroupMAC
REGISTRY["gacg_mac"] = GroupMessageMAC
REGISTRY["Ltscg_mac"] = LTSCG_GraphMAC