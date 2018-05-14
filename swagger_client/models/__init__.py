# coding: utf-8

# flake8: noqa
"""
    Web-API

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/v5...  As a quick test try reaching the route http:/localhost:8080/api/v5/info (remember that you can only access \\\"localhost\\\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # List endpoints Lots of objects offer an endpoint to list all objects (e.g. `GET: /world` to get all worlds). These endpoints return only the properties marked 'required' by default, because the list might be quite large. If you want to return ALL data for a list endpoint add the query parameter `details`, (e.g. `GET: /world?details`).  > Remember that in this case the data returned by the endpoint might be quite large.  # Debugging endpoints Apart from the `?details` flag you can also pass some other flags for debugging purposes. Remember that you must include the first query parameter with `?`, and further ones with `&`:  `details`: Includes details for list endpoints  `accept=[json/xml]`: Manually set the accept content type. This is good for browser testing, **BUT DON'T USE THIS IN PRODUCTION, YOU CAN SUPPLY THE `Accepts` HEADER FOR THAT**  `pretty`: Pretty prints the data, also good for debugging in the browser.  An example request might look like this: `http://localhost:8080/api/v5/world?details&accpet=json&pretty&key=MY-API-KEY`  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md)  # noqa: E501

    OpenAPI spec version: @version@
    Contact: inithilian@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.accepts_items import AcceptsItems
from swagger_client.models.account import Account
from swagger_client.models.advancement import Advancement
from swagger_client.models.ageable_data import AgeableData
from swagger_client.models.armor_slot_type import ArmorSlotType
from swagger_client.models.armor_stand_data import ArmorStandData
from swagger_client.models.authentication_request import AuthenticationRequest
from swagger_client.models.banner_data import BannerData
from swagger_client.models.beacon_data import BeaconData
from swagger_client.models.block_operation import BlockOperation
from swagger_client.models.block_state import BlockState
from swagger_client.models.breathing_data import BreathingData
from swagger_client.models.brewing_stand_data import BrewingStandData
from swagger_client.models.cached_object import CachedObject
from swagger_client.models.career import Career
from swagger_client.models.catalog_type import CatalogType
from swagger_client.models.catalog_type_advancement_tree import CatalogTypeAdvancementTree
from swagger_client.models.catalog_type_difficulty import CatalogTypeDifficulty
from swagger_client.models.catalog_type_dimension_type import CatalogTypeDimensionType
from swagger_client.models.catalog_type_game_mode import CatalogTypeGameMode
from swagger_client.models.catalog_type_generator_type import CatalogTypeGeneratorType
from swagger_client.models.catalog_type_item_type import CatalogTypeItemType
from swagger_client.models.catalog_type_weather import CatalogTypeWeather
from swagger_client.models.cause import Cause
from swagger_client.models.chunk import Chunk
from swagger_client.models.color import Color
from swagger_client.models.command import Command
from swagger_client.models.command_call import CommandCall
from swagger_client.models.command_data import CommandData
from swagger_client.models.command_result import CommandResult
from swagger_client.models.create_block_operation_request import CreateBlockOperationRequest
from swagger_client.models.create_entity_request import CreateEntityRequest
from swagger_client.models.create_world_request import CreateWorldRequest
from swagger_client.models.currency import Currency
from swagger_client.models.damage_request import DamageRequest
from swagger_client.models.damageable_data import DamageableData
from swagger_client.models.despawn_delay_data import DespawnDelayData
from swagger_client.models.durability_data import DurabilityData
from swagger_client.models.dye_color import DyeColor
from swagger_client.models.enchantment import Enchantment
from swagger_client.models.end_gateway_data import EndGatewayData
from swagger_client.models.entity import Entity
from swagger_client.models.entity_archtype import EntityArchtype
from swagger_client.models.entity_snapshot import EntitySnapshot
from swagger_client.models.equipment_slot_type import EquipmentSlotType
from swagger_client.models.execute_command_request import ExecuteCommandRequest
from swagger_client.models.execute_command_response import ExecuteCommandResponse
from swagger_client.models.execute_method_param import ExecuteMethodParam
from swagger_client.models.execute_method_request import ExecuteMethodRequest
from swagger_client.models.execute_method_response import ExecuteMethodResponse
from swagger_client.models.experience_holder_data import ExperienceHolderData
from swagger_client.models.falling_block_data import FallingBlockData
from swagger_client.models.firework_effect import FireworkEffect
from swagger_client.models.firework_rocket_data import FireworkRocketData
from swagger_client.models.fluid_stack import FluidStack
from swagger_client.models.food_data import FoodData
from swagger_client.models.furnace_data import FurnaceData
from swagger_client.models.fuse_data import FuseData
from swagger_client.models.game_mode import GameMode
from swagger_client.models.growth_data import GrowthData
from swagger_client.models.gui_id_property import GuiIdProperty
from swagger_client.models.health_data import HealthData
from swagger_client.models.hide_data import HideData
from swagger_client.models.horse_data import HorseData
from swagger_client.models.husky_crates_crate import HuskyCratesCrate
from swagger_client.models.husky_crates_crate_reward import HuskyCratesCrateReward
from swagger_client.models.husky_crates_crate_reward_object import HuskyCratesCrateRewardObject
from swagger_client.models.identifiable import Identifiable
from swagger_client.models.igniteable_data import IgniteableData
from swagger_client.models.inline_response_400 import InlineResponse400
from swagger_client.models.inline_response_401 import InlineResponse401
from swagger_client.models.inline_response_403 import InlineResponse403
from swagger_client.models.inline_response_404 import InlineResponse404
from swagger_client.models.inline_response_500 import InlineResponse500
from swagger_client.models.inline_response_501 import InlineResponse501
from swagger_client.models.interactive_message import InteractiveMessage
from swagger_client.models.interactive_message_option import InteractiveMessageOption
from swagger_client.models.inventory import Inventory
from swagger_client.models.inventory_capacity import InventoryCapacity
from swagger_client.models.inventory_dimension import InventoryDimension
from swagger_client.models.inventory_title import InventoryTitle
from swagger_client.models.invisibility_data import InvisibilityData
from swagger_client.models.invulnerability_data import InvulnerabilityData
from swagger_client.models.item_stack import ItemStack
from swagger_client.models.join_data import JoinData
from swagger_client.models.leash_data import LeashData
from swagger_client.models.local_date import LocalDate
from swagger_client.models.location import Location
from swagger_client.models.mmc_restrict_item import MMCRestrictItem
from swagger_client.models.mmc_tickets_ticket import MMCTicketsTicket
from swagger_client.models.message import Message
from swagger_client.models.minecart_block_data import MinecartBlockData
from swagger_client.models.mob_spawner_data import MobSpawnerData
from swagger_client.models.modify_block_operation_request import ModifyBlockOperationRequest
from swagger_client.models.nucleus_kit import NucleusKit
from swagger_client.models.nucleus_mail_message import NucleusMailMessage
from swagger_client.models.nucleus_named_location import NucleusNamedLocation
from swagger_client.models.pattern_layer import PatternLayer
from swagger_client.models.permission_struct import PermissionStruct
from swagger_client.models.pickup_delay_data import PickupDelayData
from swagger_client.models.player import Player
from swagger_client.models.plugin_container import PluginContainer
from swagger_client.models.plugin_dependency import PluginDependency
from swagger_client.models.potion_effect import PotionEffect
from swagger_client.models.red_protect_region import RedProtectRegion
from swagger_client.models.server_info import ServerInfo
from swagger_client.models.server_property import ServerProperty
from swagger_client.models.server_report import ServerReport
from swagger_client.models.server_stat import ServerStat
from swagger_client.models.server_stat_double import ServerStatDouble
from swagger_client.models.server_stat_integer import ServerStatInteger
from swagger_client.models.server_stats import ServerStats
from swagger_client.models.slime_data import SlimeData
from swagger_client.models.slot_index import SlotIndex
from swagger_client.models.slot_pos import SlotPos
from swagger_client.models.slot_side import SlotSide
from swagger_client.models.stat import Stat
from swagger_client.models.structure_data import StructureData
from swagger_client.models.subject import Subject
from swagger_client.models.subject_collection import SubjectCollection
from swagger_client.models.table_entry import TableEntry
from swagger_client.models.table_entry_entity_archetype import TableEntryEntityArchetype
from swagger_client.models.tameable_data import TameableData
from swagger_client.models.tile_entity import TileEntity
from swagger_client.models.time_holder import TimeHolder
from swagger_client.models.trade_offer import TradeOffer
from swagger_client.models.transform import Transform
from swagger_client.models.universal_market_item import UniversalMarketItem
from swagger_client.models.update_entity_request import UpdateEntityRequest
from swagger_client.models.update_player_request import UpdatePlayerRequest
from swagger_client.models.update_world_request import UpdateWorldRequest
from swagger_client.models.user_report import UserReport
from swagger_client.models.vector2i import Vector2i
from swagger_client.models.vector3d import Vector3d
from swagger_client.models.vector3i import Vector3i
from swagger_client.models.vehicle_data import VehicleData
from swagger_client.models.web_books_book import WebBooksBook
from swagger_client.models.wire_attachment_data import WireAttachmentData
from swagger_client.models.world import World
from swagger_client.models.world_border import WorldBorder
from swagger_client.models.chat_message import ChatMessage
from swagger_client.models.husky_crates_command_reward import HuskyCratesCommandReward
from swagger_client.models.husky_crates_item_reward import HuskyCratesItemReward
from swagger_client.models.player_full import PlayerFull
from swagger_client.models.world_full import WorldFull
