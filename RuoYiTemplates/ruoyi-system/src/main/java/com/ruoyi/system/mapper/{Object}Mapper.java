package com.ruoyi.system.mapper;

import com.ruoyi.system.domain.{Object};
import java.util.List;	

/**
 * 部门 数据层
 * 
 * @author ruoyi
 * @date 2019-06-19
 */
public interface {Object}Mapper 
{
	/**
     * 查询部门信息
     * 
     * @param {object}Id 部门ID
     * @return 部门信息
     */
	public {Object} select{Object}ById(Long {object}Id);
	
	/**
     * 查询部门列表
     * 
     * @param {object} 部门信息
     * @return 部门集合
     */
	public List<{Object}> select{Object}List({Object} {object});
	
	/**
     * 新增部门
     * 
     * @param {object} 部门信息
     * @return 结果
     */
	public int insert{Object}({Object} {object});
	
	/**
     * 修改部门
     * 
     * @param {object} 部门信息
     * @return 结果
     */
	public int update{Object}({Object} {object});
	
	/**
     * 删除部门
     * 
     * @param {object}Id 部门ID
     * @return 结果
     */
	public int delete{Object}ById(Long {object}Id);
	
	/**
     * 批量删除部门
     * 
     * @param {object}Ids 需要删除的数据ID
     * @return 结果
     */
	public int delete{Object}ByIds(String[] {object}Ids);
	
}