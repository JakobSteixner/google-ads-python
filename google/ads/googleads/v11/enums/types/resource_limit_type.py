# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v11.enums",
    marshal="google.ads.googleads.v11",
    manifest={"ResourceLimitTypeEnum",},
)


class ResourceLimitTypeEnum(proto.Message):
    r"""Container for enum describing possible resource limit types.
    """

    class ResourceLimitType(proto.Enum):
        r"""Resource limit type."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGNS_PER_CUSTOMER = 2
        BASE_CAMPAIGNS_PER_CUSTOMER = 3
        EXPERIMENT_CAMPAIGNS_PER_CUSTOMER = 105
        HOTEL_CAMPAIGNS_PER_CUSTOMER = 4
        SMART_SHOPPING_CAMPAIGNS_PER_CUSTOMER = 5
        AD_GROUPS_PER_CAMPAIGN = 6
        AD_GROUPS_PER_SHOPPING_CAMPAIGN = 8
        AD_GROUPS_PER_HOTEL_CAMPAIGN = 9
        REPORTING_AD_GROUPS_PER_LOCAL_CAMPAIGN = 10
        REPORTING_AD_GROUPS_PER_APP_CAMPAIGN = 11
        MANAGED_AD_GROUPS_PER_SMART_CAMPAIGN = 52
        AD_GROUP_CRITERIA_PER_CUSTOMER = 12
        BASE_AD_GROUP_CRITERIA_PER_CUSTOMER = 13
        EXPERIMENT_AD_GROUP_CRITERIA_PER_CUSTOMER = 107
        AD_GROUP_CRITERIA_PER_CAMPAIGN = 14
        CAMPAIGN_CRITERIA_PER_CUSTOMER = 15
        BASE_CAMPAIGN_CRITERIA_PER_CUSTOMER = 16
        EXPERIMENT_CAMPAIGN_CRITERIA_PER_CUSTOMER = 108
        WEBPAGE_CRITERIA_PER_CUSTOMER = 17
        BASE_WEBPAGE_CRITERIA_PER_CUSTOMER = 18
        EXPERIMENT_WEBPAGE_CRITERIA_PER_CUSTOMER = 19
        COMBINED_AUDIENCE_CRITERIA_PER_AD_GROUP = 20
        CUSTOMER_NEGATIVE_PLACEMENT_CRITERIA_PER_CUSTOMER = 21
        CUSTOMER_NEGATIVE_YOUTUBE_CHANNEL_CRITERIA_PER_CUSTOMER = 22
        CRITERIA_PER_AD_GROUP = 23
        LISTING_GROUPS_PER_AD_GROUP = 24
        EXPLICITLY_SHARED_BUDGETS_PER_CUSTOMER = 25
        IMPLICITLY_SHARED_BUDGETS_PER_CUSTOMER = 26
        COMBINED_AUDIENCE_CRITERIA_PER_CAMPAIGN = 27
        NEGATIVE_KEYWORDS_PER_CAMPAIGN = 28
        NEGATIVE_PLACEMENTS_PER_CAMPAIGN = 29
        GEO_TARGETS_PER_CAMPAIGN = 30
        NEGATIVE_IP_BLOCKS_PER_CAMPAIGN = 32
        PROXIMITIES_PER_CAMPAIGN = 33
        LISTING_SCOPES_PER_SHOPPING_CAMPAIGN = 34
        LISTING_SCOPES_PER_NON_SHOPPING_CAMPAIGN = 35
        NEGATIVE_KEYWORDS_PER_SHARED_SET = 36
        NEGATIVE_PLACEMENTS_PER_SHARED_SET = 37
        SHARED_SETS_PER_CUSTOMER_FOR_TYPE_DEFAULT = 40
        SHARED_SETS_PER_CUSTOMER_FOR_NEGATIVE_PLACEMENT_LIST_LOWER = 41
        HOTEL_ADVANCE_BOOKING_WINDOW_BID_MODIFIERS_PER_AD_GROUP = 44
        BIDDING_STRATEGIES_PER_CUSTOMER = 45
        BASIC_USER_LISTS_PER_CUSTOMER = 47
        LOGICAL_USER_LISTS_PER_CUSTOMER = 48
        RULE_BASED_USER_LISTS_PER_CUSTOMER = 153
        BASE_AD_GROUP_ADS_PER_CUSTOMER = 53
        EXPERIMENT_AD_GROUP_ADS_PER_CUSTOMER = 54
        AD_GROUP_ADS_PER_CAMPAIGN = 55
        TEXT_AND_OTHER_ADS_PER_AD_GROUP = 56
        IMAGE_ADS_PER_AD_GROUP = 57
        SHOPPING_SMART_ADS_PER_AD_GROUP = 58
        RESPONSIVE_SEARCH_ADS_PER_AD_GROUP = 59
        APP_ADS_PER_AD_GROUP = 60
        APP_ENGAGEMENT_ADS_PER_AD_GROUP = 61
        LOCAL_ADS_PER_AD_GROUP = 62
        VIDEO_ADS_PER_AD_GROUP = 63
        LEAD_FORM_CAMPAIGN_ASSETS_PER_CAMPAIGN = 143
        PROMOTION_CUSTOMER_ASSETS_PER_CUSTOMER = 79
        PROMOTION_CAMPAIGN_ASSETS_PER_CAMPAIGN = 80
        PROMOTION_AD_GROUP_ASSETS_PER_AD_GROUP = 81
        CALLOUT_CUSTOMER_ASSETS_PER_CUSTOMER = 134
        CALLOUT_CAMPAIGN_ASSETS_PER_CAMPAIGN = 135
        CALLOUT_AD_GROUP_ASSETS_PER_AD_GROUP = 136
        SITELINK_CUSTOMER_ASSETS_PER_CUSTOMER = 137
        SITELINK_CAMPAIGN_ASSETS_PER_CAMPAIGN = 138
        SITELINK_AD_GROUP_ASSETS_PER_AD_GROUP = 139
        STRUCTURED_SNIPPET_CUSTOMER_ASSETS_PER_CUSTOMER = 140
        STRUCTURED_SNIPPET_CAMPAIGN_ASSETS_PER_CAMPAIGN = 141
        STRUCTURED_SNIPPET_AD_GROUP_ASSETS_PER_AD_GROUP = 142
        MOBILE_APP_CUSTOMER_ASSETS_PER_CUSTOMER = 144
        MOBILE_APP_CAMPAIGN_ASSETS_PER_CAMPAIGN = 145
        MOBILE_APP_AD_GROUP_ASSETS_PER_AD_GROUP = 146
        HOTEL_CALLOUT_CUSTOMER_ASSETS_PER_CUSTOMER = 147
        HOTEL_CALLOUT_CAMPAIGN_ASSETS_PER_CAMPAIGN = 148
        HOTEL_CALLOUT_AD_GROUP_ASSETS_PER_AD_GROUP = 149
        CALL_CUSTOMER_ASSETS_PER_CUSTOMER = 150
        CALL_CAMPAIGN_ASSETS_PER_CAMPAIGN = 151
        CALL_AD_GROUP_ASSETS_PER_AD_GROUP = 152
        PRICE_CUSTOMER_ASSETS_PER_CUSTOMER = 154
        PRICE_CAMPAIGN_ASSETS_PER_CAMPAIGN = 155
        PRICE_AD_GROUP_ASSETS_PER_AD_GROUP = 156
        PAGE_FEED_ASSET_SETS_PER_CUSTOMER = 157
        DYNAMIC_EDUCATION_FEED_ASSET_SETS_PER_CUSTOMER = 158
        ASSETS_PER_PAGE_FEED_ASSET_SET = 159
        ASSETS_PER_DYNAMIC_EDUCATION_FEED_ASSET_SET = 160
        DYNAMIC_REAL_ESTATE_ASSET_SETS_PER_CUSTOMER = 161
        ASSETS_PER_DYNAMIC_REAL_ESTATE_ASSET_SET = 162
        DYNAMIC_CUSTOM_ASSET_SETS_PER_CUSTOMER = 163
        ASSETS_PER_DYNAMIC_CUSTOM_ASSET_SET = 164
        DYNAMIC_HOTELS_AND_RENTALS_ASSET_SETS_PER_CUSTOMER = 165
        ASSETS_PER_DYNAMIC_HOTELS_AND_RENTALS_ASSET_SET = 166
        DYNAMIC_LOCAL_ASSET_SETS_PER_CUSTOMER = 167
        ASSETS_PER_DYNAMIC_LOCAL_ASSET_SET = 168
        DYNAMIC_FLIGHTS_ASSET_SETS_PER_CUSTOMER = 169
        ASSETS_PER_DYNAMIC_FLIGHTS_ASSET_SET = 170
        DYNAMIC_TRAVEL_ASSET_SETS_PER_CUSTOMER = 171
        ASSETS_PER_DYNAMIC_TRAVEL_ASSET_SET = 172
        DYNAMIC_JOBS_ASSET_SETS_PER_CUSTOMER = 173
        ASSETS_PER_DYNAMIC_JOBS_ASSET_SET = 174
        VERSIONS_PER_AD = 82
        USER_FEEDS_PER_CUSTOMER = 90
        SYSTEM_FEEDS_PER_CUSTOMER = 91
        FEED_ATTRIBUTES_PER_FEED = 92
        FEED_ITEMS_PER_CUSTOMER = 94
        CAMPAIGN_FEEDS_PER_CUSTOMER = 95
        BASE_CAMPAIGN_FEEDS_PER_CUSTOMER = 96
        EXPERIMENT_CAMPAIGN_FEEDS_PER_CUSTOMER = 109
        AD_GROUP_FEEDS_PER_CUSTOMER = 97
        BASE_AD_GROUP_FEEDS_PER_CUSTOMER = 98
        EXPERIMENT_AD_GROUP_FEEDS_PER_CUSTOMER = 110
        AD_GROUP_FEEDS_PER_CAMPAIGN = 99
        FEED_ITEM_SETS_PER_CUSTOMER = 100
        FEED_ITEMS_PER_FEED_ITEM_SET = 101
        CAMPAIGN_EXPERIMENTS_PER_CUSTOMER = 112
        EXPERIMENT_ARMS_PER_VIDEO_EXPERIMENT = 113
        OWNED_LABELS_PER_CUSTOMER = 115
        LABELS_PER_CAMPAIGN = 117
        LABELS_PER_AD_GROUP = 118
        LABELS_PER_AD_GROUP_AD = 119
        LABELS_PER_AD_GROUP_CRITERION = 120
        TARGET_CUSTOMERS_PER_LABEL = 121
        KEYWORD_PLANS_PER_USER_PER_CUSTOMER = 122
        KEYWORD_PLAN_AD_GROUP_KEYWORDS_PER_KEYWORD_PLAN = 123
        KEYWORD_PLAN_AD_GROUPS_PER_KEYWORD_PLAN = 124
        KEYWORD_PLAN_NEGATIVE_KEYWORDS_PER_KEYWORD_PLAN = 125
        KEYWORD_PLAN_CAMPAIGNS_PER_KEYWORD_PLAN = 126
        CONVERSION_ACTIONS_PER_CUSTOMER = 128
        BATCH_JOB_OPERATIONS_PER_JOB = 130
        BATCH_JOBS_PER_CUSTOMER = 131
        HOTEL_CHECK_IN_DATE_RANGE_BID_MODIFIERS_PER_AD_GROUP = 132


__all__ = tuple(sorted(__protobuf__.manifest))
