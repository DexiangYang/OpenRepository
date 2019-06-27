package com.ruoyi.system.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.ruoyi.common.core.domain.BaseEntity;


public class {Object} extends BaseEntity
{
	private static final long serialVersionUID = 1L;
	
	private Long {object}Id;

	{dateDefine}

	public void set{Object}Id(Long {object}Id) 
	{
		this.{object}Id = {object}Id;
	}

	public Long get{Object}Id() 
	{
		return {object}Id;
	}

	{functionDefine}

    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
			.append("{object}Id", get{Object}Id())
			{appendListDefine}
            .toString();
    }
}
