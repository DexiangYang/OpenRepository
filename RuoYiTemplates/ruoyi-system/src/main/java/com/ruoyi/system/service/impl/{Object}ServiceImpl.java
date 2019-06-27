package com.ruoyi.system.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.system.mapper.{Object}Mapper;
import com.ruoyi.system.domain.{Object};
import com.ruoyi.system.service.I{Object}Service;
import com.ruoyi.common.core.text.Convert;

/**
 * 部门 服务层实现
 * 
 * @author ruoyi
 * @date 2019-06-19
 */
@Service
public class {Object}ServiceImpl implements I{Object}Service 
{
	@Autowired
	private {Object}Mapper {object}Mapper;

	/**
     * 查询部门信息
     * 
     * @param {object}Id 部门ID
     * @return 部门信息
     */
    @Override
	public {Object} select{Object}ById(Long {object}Id)
	{
	    return {object}Mapper.select{Object}ById({object}Id);
	}
	
	/**
     * 查询部门列表
     * 
     * @param {object} 部门信息
     * @return 部门集合
     */
	@Override
	public List<{Object}> select{Object}List({Object} {object})
	{
	    return {object}Mapper.select{Object}List({object});
	}
	
    /**
     * 新增部门
     * 
     * @param {object} 部门信息
     * @return 结果
     */
	@Override
	public int insert{Object}({Object} {object})
	{
	    return {object}Mapper.insert{Object}({object});
	}
	
	/**
     * 修改部门
     * 
     * @param {object} 部门信息
     * @return 结果
     */
	@Override
	public int update{Object}({Object} {object})
	{
	    return {object}Mapper.update{Object}({object});
	}

	/**
     * 删除部门对象
     * 
     * @param ids 需要删除的数据ID
     * @return 结果
     */
	@Override
	public int delete{Object}ByIds(String ids)
	{
		return {object}Mapper.delete{Object}ByIds(Convert.toStrArray(ids));
	}
	
}
