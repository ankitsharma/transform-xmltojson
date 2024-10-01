<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/apf2doc">
        <apf2doc>
            <request>
                <sender><xsl:value-of select="request/sender"/></sender>
                <id><xsl:value-of select="request/transaction_id"/></id>
            </request>
            <acct_data>
                <client_acct_id><xsl:value-of select="acct_data/client_acct_id"/></client_acct_id>
            </acct_data>
            <acct_contact>
                <first_name><xsl:value-of select="acct_contact/first_name"/></first_name>
                <phone><xsl:value-of select="acct_contact/phone"/></phone>
                <email><xsl:value-of select="acct_contact/email"/></email>
            </acct_contact>
            <notify_tmplt_group_data>
                <notify_tmplt_group>
                    <notify_tmplt_group_id><xsl:value-of select="notify_tmplt_group_data/notify_tmplt_group/notify_tmplt_group_id"/></notify_tmplt_group_id>
                </notify_tmplt_group>
            </notify_tmplt_group_data>
            <master_plan_instance_data>
                <master_plan_instance>
                    <client_master_plan_instance_id><xsl:value-of select="master_plan_instance_data/master_plan_instance/client_master_plan_instance_id"/></client_master_plan_instance_id>
                    <dunning_state>1</dunning_state>
                    <dunning_step_description><xsl:value-of select="master_plan_instance_data/master_plan_instance/dunning_step_description"/></dunning_step_description>
                    <supp_plan_instance_data>
                        <spi_supp_fields_data>
                            <spi_supp_field>
                                <field_name><xsl:value-of select="master_plan_instance_data/master_plan_instance/supp_plan_instance_data/supp_plan_instance[1]/spi_supp_fields_data/spi_supp_field[1]/field_name"/></field_name>
                                <field_value><xsl:value-of select="master_plan_instance_data/master_plan_instance/supp_plan_instance_data/supp_plan_instance[1]/spi_supp_fields_data/spi_supp_field[1]/field_value"/></field_value>
                            </spi_supp_field>
                        </spi_supp_fields_data>
                    </supp_plan_instance_data>
                </master_plan_instance>
            </master_plan_instance_data>
            <event_data>
                <event>
                    <event_id><xsl:value-of select="event_data/event/event_id"/></event_id>
                </event>
            </event_data>
        </apf2doc>
    </xsl:template>
    
</xsl:stylesheet>

