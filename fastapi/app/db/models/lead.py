from pydantic import basemodel, emailstr
from typing import Optional

class lead(basemodel):
    # Main Content
    id: Optional[int] = 0
    email: Optional[str] = ""
    email_quality: Optional[str] = ""
    email_score: Optional[str] = ""
    customer: Optional[str] = ""
    phone: Optional[str] = ""
    phone_quality: Optional[str] = ""
    company: Optional[str] = ""
    company_name: Optional[str] = ""
    website: Optional[str] = ""
    
    # Location 
    currency: Optional[str] = ""
    opportunity: Optional[str] = ""
    city: Optional[str] = ""
    country: Optional[str] = ""
    street: Optional[str] = ""
    zip: Optional[str] = ""
    geo_latitude: Optional[str] = ""
    geo_longitude: Optional[str] = ""
    
    # Sale Details
    salesperson: Optional[str] = ""
    priority: Optional[str] = ""
    days_to_assign: Optional[str] = ""
    days_to_close: Optional[str] = ""
    days_to_convert: Optional[str] = ""
    exceeded_closing_days: Optional[str] = ""
    followers: Optional[str] = ""
    followers_partners: Optional[str] = ""
    last_updated_by: Optional[str] = ""
    last_updated_on: Optional[str] = ""
    my_activity_deadline = Optional[str] = ""
    next_activity_deadline =Optional[str] = ""
    next_activity_type: Optional[str] = ""

    # Lead Info General
    active: Optional[bool] = True
    stage: Optional[str] = ""
    user_company: Optional[str] = ""
    expected_closing: Optional[str] = ""
    expected_revenue: Optional[float] = 0
    campaign: Optional[str] = ""
    closed_date: Optional[str] = ""
    display_name: Optional[str] = ""
    has_message: Optional[str] = ""
    is_follower: Optional[str] = ""
    is_partner_visible: Optional[str] = ""
    is_won: Optional[str] = ""
    medium: Optional[str] = ""
    meeting_display_label: Optional[str] = ""
    messages: Optional[str] = ""
    probability: Optional[str] = ""
    prorated_revenue: Optional[str] = ""
    responsible_user: Optional[str] = ""
    sales_team: Optional[str] = ""
    sanitized_number: Optional[str] = ""
    source: Optional[str] = ""
    state: Optional[str] = ""
    status_time: Optional[str] = ""
    tags: Optional[str] = ""
    type: Optional[str] = ""
    number_of_quotations: Optional[str] = ""
    number_of_sale_orders: Optional[str] = ""
    created_by: Optional[str] = ""
    created_on: Optional[str] = ""

    # Meta Data
    page_views: Optional[int] = 0
    registrations: Optional[int] = 0
    sessions: Optional[int] = 0
    activities: Optional[str] = ""
    activity_state: Optional[str] = ""
    activity_type_icon: Optional[str] = ""
    assignment_date: Optional[str] = ""
    attachment_count: Optional[str] = ""
    automated_probability: Optional[str] = ""
    bounce: Optional[str] = ""
    color_index: Optional[str] = ""
    email_domain_criterion: Optional[str] = ""
    external_id: Optional[str] = ""
    iap_credits: Optional[str] = ""
    is_automated_probability: Optional[str] = ""
    kanban_state: Optional[str] = ""
    language: Optional[str] = ""
    locale_code: Optional[str] = ""
    number_of_actions: Optional[str] = ""
    number_of_errors: Optional[str] = ""
    number_of_rental_orders: Optional[str] = ""
    number_of_rental_quotations: Optional[str] = ""
